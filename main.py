# main.py
import argparse
import json
import logging

from data_synthesizer import generate_test_data
from testCase_synthesizer import generate_test_scenarios

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def save_to_file(filename: str, data: dict | list):
    """Saves data to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logging.info(f"Successfully saved output to {filename}")
    except IOError as e:
        logging.error(f"Error saving file: {e}")

def main():
    parser = argparse.ArgumentParser(description="GenAI Test Data & Scenario Synthesizer")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sub-parser for generating data
    data_parser = subparsers.add_parser("data", help="Generate synthetic test data")
    data_parser.add_argument("--schema", type=str, required=True, help="String describing the JSON schema, e.g., \"{'name': 'string', 'email': 'email'}\"")
    data_parser.add_argument("--count", type=int, required=True, help="Number of data items to generate")
    data_parser.add_argument("--context", type=str, default="", help="Optional context for data generation")
    data_parser.add_argument("--out", type=str, default="test_data.json", help="Output file name")

    # Sub-parser for generating scenarios
    scenario_parser = subparsers.add_parser("scenario", help="Generate test scenarios")
    scenario_parser.add_argument("--feature", type=str, required=True, help="Description of the feature to test")
    scenario_parser.add_argument("--types", type=str, default="happy_path,negative,edge_case", help="Comma-separated list of scenario types (e.g., happy_path,negative)")
    scenario_parser.add_argument("--out", type=str, default="test_scenarios.json", help="Output file name")

    args = parser.parse_args()

    if args.command == "data":
        generated_data = generate_test_data(args.schema, args.count, args.context)
        if generated_data:
            save_to_file(args.out, generated_data)
    elif args.command == "scenario":
        scenario_types = [t.strip() for t in args.types.split(',')]
        generated_scenarios = generate_test_scenarios(args.feature, scenario_types)
        if generated_scenarios:
            save_to_file(args.out, generated_scenarios)

if __name__ == "__main__":
    main()
