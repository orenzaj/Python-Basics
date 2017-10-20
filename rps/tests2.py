# We haven't used assertTrue yet but I'm sure you can handle this. assertTrue checks that a value is truthy. Complete the first test using assertTrue. Provide your own good palindrome or use "tacocat".
import unittest

from string_fun import is_palindrome


class PalindromeTestCase(unittest.TestCase):
    def test_good_palindrome(self):
        assert self.assertTrue(is_palindrome())
      
    def test_bad_palindrome(self):
        assert self.assertFalse(is_palindrome())

