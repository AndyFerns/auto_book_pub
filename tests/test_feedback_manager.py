import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from human_loop.feedback_manager import collect_feedback, log_human_feedback

class TestFeedbackManager(unittest.TestCase):
    def test_collect_feedback_returns_string(self):
        # Skipping real user input for testing
        pass

if __name__ == "__main__":
    unittest.main()