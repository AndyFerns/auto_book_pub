# tests/test_writer_agent.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from ai_agents.writer_agent import WriterAgent

class TestWriterAgent(unittest.TestCase):
    @patch('ai_agents.writer_agent.WriterAgent.spin')
    def test_spin_returns_rewritten_text(self, mock_spin):
        # Arrange: Set up mock return value
        input_text = "The sun was setting over the hills."
        mock_spin.return_value = "The golden sun dipped behind the quiet hills."

        # Act
        writer = WriterAgent()
        output = writer.spin(input_text)

        # Assert
        self.assertEqual(output, "The golden sun dipped behind the quiet hills.")

if __name__ == "__main__":
    unittest.main()
