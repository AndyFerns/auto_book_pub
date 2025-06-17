import time
import logging
import os
import google.generativeai as genai
from ollama import Client, ResponseError
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Load Gemini API key if available
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


class WriterAgent:
    def __init__(self):
        self.use_gemini = GEMINI_API_KEY is not None
        self.client = Client()
        self.model = "mistral"

    def spin(self, text):
        logging.info(f"Using model: {'Gemini' if self.use_gemini else self.model} for WriterAgent")
        start = time.time()

        # First try Gemini
        if self.use_gemini:
            try:
                gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")
                response = gemini_model.generate_content(
                    f"Rewrite the following text with creative flair, enhancing readability while keeping the core meaning intact:\n{text}"
                )
                end = time.time()
                logging.info(f"[✅] Writing done in {end - start:.2f}s using Gemini")
                return response.text
            except Exception as e:
                logging.error(f"[❌] Gemini API failed: {e}. Falling back to local model.")
                self.use_gemini = False  # fallback to local if error occurs

        # Fallback to local Ollama model (mistral → gemma:2b)
        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a creative writer. Rewrite the input text with better language, clarity, and emotional tone."},
                    {"role": "user", "content": text}
                ]
            )
        except ResponseError:
            logging.warning("WriterAgent failed on mistral due to resource limits. Falling back to gemma:2b")
            self.model = "gemma:2b"
            response = self.client.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a creative writer. Rewrite the input text with better language, clarity, and emotional tone."},
                    {"role": "user", "content": text}
                ]
            )

        end = time.time()
        logging.info(f"[✅] Writing done in {end - start:.2f}s using Ollama ({self.model})")
        return response['message']['content']
