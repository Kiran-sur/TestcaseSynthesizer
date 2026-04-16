# llm_client.py
import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class LLMClient:
    """A client for interacting with the Google Gemini Pro model."""

    def __init__(self):
        """Initializes the LLM client and configures the API key."""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")
        
        genai.configure(api_key=api_key)
        
        # Configuration for deterministic and structured output (JSON)
        generation_config = {
            "temperature": 0.2, # Lower temperature for less "creative" and more factual output
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 2048,
            "response_mime_type": "application/json", # Crucial for getting JSON output
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-pro",
            generation_config=generation_config
        )
        logging.info("LLM Client initialized successfully.")

    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to the LLM and returns the generated text.

        Args:
            prompt: The prompt to send to the model.

        Returns:
            The model's response as a string.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logging.error(f"An error occurred during LLM generation: {e}")
            return "" # Return empty string on failure

# Singleton instance to be used across the application
llm_client = LLMClient()
 