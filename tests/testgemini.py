import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


# # Load API Key from environment
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# if not GEMINI_API_KEY:
#     raise RuntimeError("GEMINI_API_KEY is not set in environment variables.")

# # Configure Gemini API
# genai.configure(api_key=GEMINI_API_KEY)


# # models = genai.list_models()
# # for model in models:
# #     print(model.name, model.supported_generation_methods)

# def test_gemini():
#     try:
#         model = genai.GenerativeModel("models/gemini-1.5-flash")  # NOTE: use full model name
#         response = model.generate_content("Hello! Can you summarize what Gemini is?")
#         print("✅ Gemini API key works. Response:")
#         print(response.text)
#     except Exception as e:
#         print(f"❌ Gemini API key failed: {e}")


class TestGeminiAPI(unittest.TestCase):
    def test_gemini_response(self):
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            self.skipTest("GEMINI_API_KEY not set")
        genai.configure(api_key=key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content("Say hello world")
        self.assertIn("hello", response.text.lower())

if __name__ == "__main__":
    unittest.main()
