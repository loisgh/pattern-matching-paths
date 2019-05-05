import unittest
from Pattern import *
# import mock


class PatternTests(unittest.TestCase):

    def test_sort(self):
        pat = Pattern()
        expected_result = {'*': ['*,b,*']}
        expected_len = 5
        actual_result, actual_len = pat.sort_by_length('*,b,*', {})
        self.assertEqual(actual_len, expected_len)
        self.assertDictEqual(actual_result, expected_result)
