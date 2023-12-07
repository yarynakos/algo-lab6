import unittest
from src.main import boyer_moore


class TestBoyerMooreSearch(unittest.TestCase):
    def test_search_single_occurrence(self):
        haystack = "ababcababcabcabc"
        needle = "abc"
        result = boyer_moore(haystack, needle)
        self.assertEqual(result, [2, 7, 10, 13])

    def test_search_occurrence(self):
        haystack = "babcababcabcabcabc"
        needle = "abc"
        result = boyer_moore(haystack, needle)
        self.assertEqual(result, [1, 6, 9, 12, 15])

    def test_search_no_occurrence(self):
        haystack = "abcdefgh"
        needle = "xyz"
        result = boyer_moore(haystack, needle)
        self.assertEqual(result, [])
