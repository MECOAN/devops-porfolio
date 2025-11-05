"""
Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

Examples:

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams.
Input: s1 = "allergy", s2 = "allergyy" 
Output: false 
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams. 
Input: s1 = "listen", s2 = "lists" 
Output: false 
Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.
Constraints:
1 ≤ s1.size(), s2.size() ≤ 10^5
s1, s2 consists of lowercase English letters.
"""

from src.python.Anagram import Solution
from tests.python.util import create_string

sol = Solution()

# Sanity tests scenarios
def test_sanity_scenarios():
    assert sol.areAnagrams("geeks", "kseeg") == True
    assert sol.areAnagrams("allergy", "allergyy") == False
    assert sol.areAnagrams("listen", "lists") == False

# Strings with different length
def test_different_length():
    assert sol.areAnagrams("asd", "aasd") == False
    assert sol.areAnagrams("elements", "element") == False

# Same length but different characters
def test_different_characters():
    assert sol.areAnagrams("asdfgh", "asdfgj") == False
    assert sol.areAnagrams("asdfgj", "asdfgi") == False

# Strings with only one character
def test_only_one_character():
    assert sol.areAnagrams("a", "a") == True
    assert sol.areAnagrams("a", "b") == False

# Srtrings very large
def test_very_large_strings():
    string1 = create_string(100000, ["a","s","d","h","c","v","m","n","q","w","e","p","o","i","g","f"])
    string2 = create_string(100000, ["g","i","o","p","e","w","q","n","m","v","c","h","d","s","a","f"])
    assert sol.areAnagrams(string1, string2) == True
    string1 = create_string(99999, ["a","s","d","h","c","v","m","n","q","w","e","p","o","i","g","f"])
    string1 = string1 + "q"
    string2 = create_string(100000, ["g","i","o","p","e","w","q","n","m","v","c","h","d","s","a","f"])
    assert sol.areAnagrams(string1, string2) == False
