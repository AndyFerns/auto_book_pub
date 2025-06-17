import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from rl_search.retriever import retrieve_version

class TestRetriever(unittest.TestCase):
    def test_retrieve_version_type(self):
        result = retrieve_version("test query", top_k=1)
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()