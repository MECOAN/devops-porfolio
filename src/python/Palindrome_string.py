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

class Solution:
    def isPalindrome(self, s):
        total = len(s)
        mid = total // 2
        if(total % 2 != 0):
            mid+=1
        
        for i in range(mid):
            last = (total-1-i)
            if(s[i] != s[last]):
                return False
        return True
