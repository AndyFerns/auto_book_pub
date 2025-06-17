# ai_agents/reviewer_agent.py

import logging
import google.generativeai as genai
import os
from ollama import Client
from dotenv import load_dotenv
import time

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s') #script logging

class ReviewerAgent:
    def __init__(self):
        self.use_gemini = GEMINI_API_KEY is not None
        self.client = Client()
        self.model = "gemma:2b"

    def review(self, text):
        logging.info(f"Using model: {'Gemini' if self.use_gemini else self.model} for ReviewerAgent")
        start = time.time()

        if self.use_gemini:
            try:
                gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")
                response = gemini_model.generate_content(
                    f"Improve grammar, clarity, and flow in the following text without altering its meaning:\n{text}"
                )
                end = time.time()
                logging.info(f"[✅] Reviewing done in {end - start:.2f}s")
                return response.text
            except Exception as e:
                logging.error(f"Gemini API failed: {e}. Falling back to local model.")
                self.use_gemini = False

        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a senior editor. Refine the following content for publication quality. Fix tone, grammar, and structure."},
                {"role": "user", "content": text}
            ]
        )
        end = time.time()
        logging.info(f"[✅] Reviewing done in {end - start:.2f}s")
        return response['message']['content']
