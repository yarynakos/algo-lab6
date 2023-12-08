import unittest
from src.main import boyer_moore, build_shift_table


class TestBoyerMooreSearch(unittest.TestCase):
    def test_search_single_occurrence(self):
        haystack = "ababcababcabcabc"
        needle = "abc"
        shift_table = build_shift_table(needle)
        result = boyer_moore(haystack, needle, shift_table)
        self.assertEqual(result, [2, 7, 10, 13])

    def test_search_occurrence(self):
        haystack = "babcababcabcabcabc"
        needle = "abc"
        shift_table = build_shift_table(needle)
        result = boyer_moore(haystack, needle, shift_table)
        self.assertEqual(result, [1, 6, 9, 12, 15])

    def test_search_no_occurrence(self):
        haystack = "abcdefgh"
        needle = "xyz"
        shift_table = build_shift_table(needle)
        result = boyer_moore(haystack, needle, shift_table)
        self.assertEqual(result, [])

    def test_search(self):
        haystack = "фхронограф"
        needle = "хронограф"
        shift_table = build_shift_table(needle)
        result = boyer_moore(haystack, needle, shift_table)
        self.assertEqual(result, [1])


    def test_shift_table(self):
        needle = "хронограф"
        shift_table = {'х': 8, 'р': 6, 'о': 4, 'н': 5, 'о': 4, 'г': 3, 'р': 2, 'а': 1}
        self.assertEqual(build_shift_table(needle), shift_table)
