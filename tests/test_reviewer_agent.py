import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from ai_agents.reviewer_agent import ReviewerAgent

class TestReviewerAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ReviewerAgent()

    def test_review_returns_string(self):
        result = self.agent.review("This is a test sentence.")
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()