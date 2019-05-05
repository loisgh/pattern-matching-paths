import unittest
from Pattern import *


class PatternTests(unittest.TestCase):

    def test_sort(self):
        pat = Pattern()
        expected_result = {'*': ['*,b,*']}
        expected_len = 5
        actual_result, actual_len = pat.sort_by_length('*,b,*', {})
        self.assertEqual(actual_len, expected_len)
        self.assertDictEqual(actual_result, expected_result)

    def test_remove_leading_slashes(self):
        pat = Pattern()
        in_path = "/w/x/y/z"
        expected_result = "w/x/y/z"
        self.assertEqual(pat.strip_off_leading_trailing_slash(in_path), expected_result)

        in_path = 'abc'
        expected_result = 'abc'
        self.assertEqual(pat.strip_off_leading_trailing_slash(in_path), expected_result)

    def test_create_the_regex(self):
        pat = Pattern()
        inpattern = '*,b,*'
        expected_regex = '^.[/][b][/].$'
        expected_idx_sum = 2
        expected_wildcard_count = 2
        the_regex, wildcard_count, idx_sum = pat.create_the_regex(inpattern)
        self.assertEqual(expected_idx_sum, idx_sum)
        self.assertEqual(expected_regex, the_regex)
        self.assertEqual(expected_wildcard_count, wildcard_count)

    def test_match_the_line(self):
        patterns =  \
            {5: {'*': ['*,b,*', '*,*,c'], 'a': ['a,*,*']},
            7: {'*': ['*,x,y,z'], 'w': ['w,x,*,*']},
            11: {'f': ['foo,bar,baz']}}

        regexes = \
            {'*,*,c': {'idx_sum': 1, 'regex': '^.[/].[/][c]$', 'wildcard_count': 2},
            '*,b,*': {'idx_sum': 2, 'regex': '^.[/][b][/].$', 'wildcard_count': 2},
            '*,x,y,z': {'idx_sum': 0, 'regex': '^.[/][x][/][y][/][z]$', 'wildcard_count': 1},
            'a,*,*': {'idx_sum': 3, 'regex': '^[a][/].[/].$', 'wildcard_count': 2},
            'foo,bar,baz': {'idx_sum': 0,'regex': '^foo[/]bar[/]baz$','wildcard_count': 0},
            'w,x,*,*': {'idx_sum': 5, 'regex': '^[w][/][x][/].[/].$', 'wildcard_count': 2}}

    def test_determine_correct_regex(self):
        pass

    def test_match_paths(self):
        pass

    def test_process_pattern(self):
        pass
    