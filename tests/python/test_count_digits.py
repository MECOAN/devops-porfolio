"""
Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.

A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
Digits of n should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.

Examples :

Input: n = 12
Output: 2
Explanation: 1, 2 when both divide 12 leaves remainder 0.
Input: n = 2446
Output: 1
Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.
Input: n = 23
Output: 0
Explanation: 2 and 3, none of them divide 23 evenly.
Constraints:
1<= n <=10^5
"""

from src.python.Count_digits import Solution

sol = Solution()

# Sanity tests scenarios
def test_sanity_scenarios():
    assert sol.evenlyDivides(12) == 2
    assert sol.evenlyDivides(2446) == 1
    assert sol.evenlyDivides(23) == 0

# Smaller possible number
def test_smaller_number():
    assert sol.evenlyDivides(1) == 1

# Bigger possible number
def test_bigger_number():
    assert sol.evenlyDivides(100000) == 1

# With different numbers
def test_multiple_numbers():
    assert sol.evenlyDivides(121524) == 5
    assert sol.evenlyDivides(123456) == 5
    assert sol.evenlyDivides(159489) == 3
    assert sol.evenlyDivides(453789) == 3
