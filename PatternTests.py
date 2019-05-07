import unittest
from Pattern import *


class PatternTests(unittest.TestCase):

    def test_sort(self):
        pat = Pattern()
        expected_result = {'*': ['*,b,*']}
        expected_len = 3
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
        expected_regex = '^.+[/]b[/].+$'
        expected_idx_sum = 2
        expected_wildcard_count = 2
        the_regex, wildcard_count, idx_sum = pat.create_the_regex(inpattern)
        self.assertEqual(expected_idx_sum, idx_sum)
        self.assertEqual(expected_regex, the_regex)
        self.assertEqual(expected_wildcard_count, wildcard_count)

    def test_match_the_line(self):
        regexes = \
            {'*,*,c': {'idx_sum': 1, 'regex': '^.+[/].+[/]c$', 'wildcard_count': 2},
             '*,b,*': {'idx_sum': 2, 'regex': '^.+[/]b[/].+$', 'wildcard_count': 2},
             '*,x,y,z': {'idx_sum': 0, 'regex': '^.+[/]x[/]y[/]z$', 'wildcard_count': 1},
             'a,*,*': {'idx_sum': 3, 'regex': '^a[/].+[/].+$', 'wildcard_count': 2},
             'foo,bar,baz': {'idx_sum': 0,
                             'regex': '^foo[/]bar[/]baz$',
                             'wildcard_count': 0},
            'w,x,*,*': {'idx_sum': 5, 'regex': '^w[/]x[/].+[/].+$', 'wildcard_count': 2},
            ' ,x,y,z': {'idx_sum': 0, 'regex': '^\\s+[/]x[/]y[/]z$', 'wildcard_count': 0},
             'foo,!@#$ %^&*(),*,baz': {'idx_sum': 2,
                                       'regex': '^foo[/]!@\\#\\$\\s+%\\^\\&\\*\\(\\)[/].+[/]baz$',
                                       'wildcard_count': 1},
             }

        patterns = \
            {3: {'*': ['*,b,*', '*,*,c'], 'a': ['a,*,*'], 'f': ['foo,bar,baz']},
             4: {'*': ['*,x,y,z'], 'w': ['w,x,*,*'], ' ': [' ,x,y,z'], 'f': ['foo,!@#$ %^&*(),*,baz']}}

        pat = Pattern()
        expected_result = '*,x,y,z'
        actual_result = pat.match_the_line('/w/x/y/z/', patterns, regexes)
        self.assertEqual(expected_result, actual_result)

        expected_result = ' ,x,y,z'
        actual_result = pat.match_the_line(' /x/y/z', patterns, regexes)
        self.assertEqual(expected_result, actual_result)

        expected_result = 'foo,!@#$ %^&*(),*,baz'
        actual_result = pat.match_the_line('foo/!@#$ %^&*()/blah/baz', patterns, regexes)
        self.assertEqual(expected_result, actual_result)