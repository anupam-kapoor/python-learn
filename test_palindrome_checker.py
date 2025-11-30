"""
Unit tests for the Palindrome Checker
"""

import unittest
from palindrome_checker import is_palindrome


class TestPalindromeChecker(unittest.TestCase):
    """Test cases for the palindrome checker function"""
    
    def test_simple_palindrome(self):
        """Test a simple single-word palindrome"""
        self.assertTrue(is_palindrome("racecar"))
    
    def test_simple_non_palindrome(self):
        """Test a simple non-palindrome word"""
        self.assertFalse(is_palindrome("hello"))
    
    def test_palindrome_with_spaces(self):
        """Test palindromes with spaces"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
    
    def test_case_insensitive(self):
        """Test that checking is case-insensitive"""
        self.assertTrue(is_palindrome("RaceCar"))
    
    def test_single_character(self):
        """Test single character is a palindrome"""
        self.assertTrue(is_palindrome("a"))
    
    def test_empty_string(self):
        """Test empty string is a palindrome"""
        self.assertTrue(is_palindrome(""))
    
    def test_two_same_characters(self):
        """Test two identical characters"""
        self.assertTrue(is_palindrome("aa"))


if __name__ == "__main__":
    unittest.main()
