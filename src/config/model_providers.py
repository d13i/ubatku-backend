import os
import base64
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def anthropic_structured_output(
        prompt: str, 
        image_base64: str, 
        json_schema: dict,
        model: str = "claude-sonnet-4-5",
        max_tokens: int = 1024,
        media_type: str = "image/jpeg"):

    """
    Generate structured JSON output from Anthropic's API using a prompt and an optional
    Base64 image input.

    https://platform.claude.com/docs/en/build-with-claude/structured-outputs
    """
    content_blocks = [
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": media_type,
                "data": image_base64
            }
        }
    ]

    messages = [
        {
            "role": "user",
            "content": content_blocks
        }
    ]

    response = client.beta.messages.create(
        model=model,
        max_tokens=max_tokens,
        betas=["structured-outputs-2025-11-13"],
        messages=messages,
        output_format={
            "type": "json_schema",
            "schema": json_schema
        }
    )
    return response.content[0].text


if __name__ == "__main__":
    # Example usages

    #########################################
    # Anthropic Structured Output with Image Input
    json_schema = {
        "type": "object",
        "properties": {
            "colours": {
                "type": "array",
                "items": {"type": "string"}
            },
            "count": {"type": "integer"},
            "thought_process": {"type": "string"} # usually include this to fine tune prompt
        },
        "required": ["colours", "count"],
        "additionalProperties": False
    }

    test = anthropic_structured_output(
        prompt="Describe the dominant colours in this image.",
        image_base64="encode from playground lol",
        json_schema=json_schema
    )

    print(test)

    ########################################
    # Some other llm api call

