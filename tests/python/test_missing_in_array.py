"""
Test scenarios for Missing in Array code
You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.
Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.
Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.
Constraints:
1 ≤ arr.size() ≤ 10a^6
1 ≤ arr[i] ≤ arr.size() + 1
"""

from src.python.Missing_in_array import Solution
from tests.python.util import get_unsorted_list_with_missing_value
sol = Solution()

#Sanity test
def test_sanity_scenarios():
    assert sol.missingNum(get_unsorted_list_with_missing_value(6, 4)) == 4
    assert sol.missingNum(get_unsorted_list_with_missing_value(9,6)) == 6

#Scenario for single value array
def test_only_one_value_scenarios():
    assert sol.missingNum([1]) == 2
    assert sol.missingNum([2]) == 1

#Scenario for bigger (10^6) array
def test_bigger_possible_array():
    assert sol.missingNum(get_unsorted_list_with_missing_value(1000001,1000000)) == 1000000
    assert sol.missingNum(get_unsorted_list_with_missing_value(1000001, 543210)) == 543210
    assert sol.missingNum(get_unsorted_list_with_missing_value(1000001, 98765)) == 98765

