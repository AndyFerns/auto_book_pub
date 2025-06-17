import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from scraping.scraper import scrape_chapter

class TestScraper(unittest.TestCase):
    def test_scrape_chapter_returns_text(self):
        result = scrape_chapter("https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()