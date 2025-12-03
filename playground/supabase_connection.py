import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool

# Load environment variables from .env file
load_dotenv()

# Fetch PostgreSQL configuration from environment variables
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")  # Default PostgreSQL port
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_POOL_SIZE = int(os.getenv("POSTGRES_POOL_SIZE", "5"))
POSTGRES_MAX_OVERFLOW = int(os.getenv("POSTGRES_MAX_OVERFLOW", "10"))

# Validate required environment variables
required_vars = {
    "POSTGRES_HOST": POSTGRES_HOST,
    "POSTGRES_DB": POSTGRES_DB,
    "POSTGRES_USER": POSTGRES_USER,
    "POSTGRES_PASSWORD": POSTGRES_PASSWORD,
}

missing_vars = [key for key, value in required_vars.items() if not value]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Create PostgreSQL connection URL
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Create SQLAlchemy engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=POSTGRES_POOL_SIZE,
    max_overflow=POSTGRES_MAX_OVERFLOW,
    pool_pre_ping=True,  # Verify connections before using them
    echo=True  # Set to False in production
)

def test_connection():
    """Test the database connection"""
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print("✓ Database connection successful!")
            print(f"PostgreSQL version: {version}")
            return True
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing PostgreSQL connection...")
    print(f"Host: {POSTGRES_HOST}")
    print(f"Database: {POSTGRES_DB}")
    print(f"User: {POSTGRES_USER}")
    print(f"Port: {POSTGRES_PORT}")
    print(f"Pool Size: {POSTGRES_POOL_SIZE}")
    print(f"Max Overflow: {POSTGRES_MAX_OVERFLOW}")
    print("-" * 50)
    
    test_connection()
