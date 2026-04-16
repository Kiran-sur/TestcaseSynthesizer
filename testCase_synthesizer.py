# testCase_synthesizer.py
import json
import logging
from llm_client import llm_client

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_test_scenarios(feature_description: str, scenario_types: list[str]) -> dict | None:
    """
    Generates test scenarios for a given feature.

    Args:
        feature_description: A description of the application feature to test.
        scenario_types: A list of scenario types to generate (e.g., 'happy path', 'edge case', 'negative').

    Returns:
        A dictionary where keys are scenario types and values are lists of scenarios, or None on failure.
    """
    types_string = ", ".join(scenario_types)
    
    prompt = f"""
    You are a world-class QA engineer. Your task is to generate test scenarios for a software feature.
    
    Feature Description: "{feature_description}"

    I need you to generate scenarios for the following categories: {types_string}.
    
    For each category, provide a list of detailed scenarios. Format each scenario using Gherkin syntax (Given/When/Then).

    Your final output must be a single, valid JSON object. The keys of the object should be the scenario categories you were asked to generate. The value for each key should be an array of strings, where each string is a complete Gherkin scenario.

    Example for a single category:
    {{
      "happy_path": [
        "Scenario: Successful login with valid credentials\\n  Given the user is on the login page\\n  When the user enters a valid username and password\\n  Then the user should be redirected to the dashboard"
      ]
    }}
    
    Do not include any explanatory text or markdown formatting outside of the JSON structure.
    """

    logging.info(f"Generating scenarios for '{feature_description}'...")
    response_text = llm_client.generate(prompt)

    if not response_text:
        logging.error("Failed to get a response from the LLM.")
        return None

    try:
        scenarios = json.loads(response_text)
        logging.info("Successfully generated and parsed scenarios.")
        return scenarios
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from LLM response: {e}\nRaw response was:\n{response_text}")
        return None
