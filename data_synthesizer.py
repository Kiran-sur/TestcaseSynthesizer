# data_synthesizer.py
import json
from llm_client import llm_client

def generate_test_data(data_schema: str, count: int, context: str = "") -> list | None:
    """
    Generates a list of structured test data items based on a schema.

    Args:
        data_schema: A string describing the desired JSON structure and data types.
                     Example: "{'name': 'string', 'age': 'integer', 'is_active': 'boolean'}"
        count: The number of data items to generate.
        context: Optional additional context for the data generation.

    Returns:
        A list of dictionaries representing the test data, or None on failure.
    """
    prompt = f"""
    You are a world-class test data synthesizer. Your task is to generate a list of {count} unique and realistic JSON objects.
    
    The JSON objects must strictly adhere to the following schema and data types:
    {data_schema}

    Additional context for data generation: {context if context else "None"}

    Ensure the output is a single, valid JSON array containing the {count} objects. Do not include any explanatory text or markdown formatting.
    """

    print(f"\n--- Generating {count} data items... ---")
    response_text = llm_client.generate(prompt)

    if not response_text:
        print("Failed to get a response from the LLM.")
        return None

    try:
        # The response should be a clean JSON string because of our model config
        data = json.loads(response_text)
        if isinstance(data, list) and len(data) == count:
            print(f"Successfully generated and parsed {len(data)} data items.")
            return data
        else:
            print(f"Generated data is not in the expected format. Expected a list of {count} items.")
            return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from LLM response: {e}")
        print(f"Raw response was:\n{response_text}")
        return None

