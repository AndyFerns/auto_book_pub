import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from versioning.chromadb_manager import save_version, list_versions

class TestChromaDBManager(unittest.TestCase):
    def test_save_and_list_versions(self):
        save_version("Test version content.")
        list_versions()

if __name__ == "__main__":
    unittest.main()