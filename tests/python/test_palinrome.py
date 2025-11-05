"""
You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

Examples :

Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
Constraints:
1 ≤ s.size() ≤ 10^6
The string s contains only lowercase english letters (a-z).
"""

from src.python.Palindrome_string import Solution
from tests.python.util import create_string, create_palindome_string

sol = Solution()

# Sanity test scenarios
def test_sanity_scenarios():
    assert sol.isPalindrome("abba") == True
    assert sol.isPalindrome("abcd") == False

# Smallest length possible string 
def test_smallest_string():
    assert sol.isPalindrome("aba") == True
    assert sol.isPalindrome("abc") == False

# Largest length possible string
def test_largest_string():
    assert sol.isPalindrome(create_string(1000000,["a","b"])) == False
    string = create_string(500000,["a","b","c","d","e","f","g","h","i","j","k","l"])
    string = create_palindome_string(string)
    assert sol.isPalindrome(string) == True

