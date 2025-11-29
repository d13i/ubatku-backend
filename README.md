# ubatku-backend

An app that reminds users to take their medication

Insert Flow:

1. Take pic of prescription
2. Pass to vlm, structured output
3. Ask for user input if have missing info
4. Additional calculations for quantity calculations
5. Send params to frontend for alarm settings
6. Additional settings to caretaker for confirmation??

Remind Flow:

1. Alarm goes off, specific quantity, method etc...
2. User required to take pic to send evidence to caretaker
3. Update backend on quantity
4. SNOOZE EMERGENCY??

Setup

1. Setup and activate venv
2. Run `pip install -r requirements.txt`
3. Create .env and insert environment variables referring to .env.example
