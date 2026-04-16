# GenAI Synthesizer

GenAI Synthesizer is a world-class tool designed to streamline software testing by leveraging the power of Google Gemini Pro. It automates the creation of realistic synthetic test data and detailed Gherkin-style test scenarios.

## Features

- **Data Synthesis**: Generate structured JSON test data based on a provided schema and item count.
- **Scenario Synthesis**: Create comprehensive test scenarios (Happy Path, Negative, Edge Case) in Gherkin syntax (Given/When/Then) for any software feature.
- **AI-Powered**: Utilizes Google's Gemini Pro model for intelligent and context-aware generation.

## Prerequisites

- Python 3.10+
- A Google Cloud project with the Generative AI API enabled.
- A Google API Key.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd genai_synthesizer
    ```

2.  **Install dependencies:**
    ```bash
    pip install google-generativeai python-dotenv
    ```

3.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

## Usage

The tool is operated via `main.py` using two primary commands: `data` and `scenario`.

### 1. Generating Test Data

Use the `data` command to generate a list of JSON objects.

```bash
python main.py data --schema "{'id': 'int', 'username': 'string', 'email': 'email'}" --count 5 --out users.json
```

**Arguments:**
- `--schema`: (Required) A string describing the JSON structure.
- `--count`: (Required) The number of items to generate.
- `--context`: (Optional) Additional context to guide the AI.
- `--out`: (Optional) Output filename (default: `test_data.json`).

### 2. Generating Test Scenarios

Use the `scenario` command to generate Gherkin test cases for a specific feature.

```bash
python main.py scenario --feature "User authentication with Two-Factor Authentication" --types "happy_path,negative" --out auth_tests.json
```

**Arguments:**
- `--feature`: (Required) Description of the feature to test.
- `--types`: (Optional) Comma-separated list of scenario types (default: `happy_path,negative,edge_case`).
- `--out`: (Optional) Output filename (default: `test_scenarios.json`).

## Project Structure

- `main.py`: CLI entry point.
- `llm_client.py`: Configuration and wrapper for the Gemini Pro API.
- `data_synthesizer.py`: Logic for generating structured synthetic data.
- `testCase_synthesizer.py`: Logic for generating Gherkin test scenarios.