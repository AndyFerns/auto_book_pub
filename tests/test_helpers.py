import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from utils.helpers import load_config

class TestHelpers(unittest.TestCase):
    def test_load_config_returns_dict(self):
        config = load_config()
        self.assertIsInstance(config, dict)

if __name__ == "__main__":
    unittest.main() 