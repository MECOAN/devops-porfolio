"""
Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.

Note: You can return the elements in any order but the driver code will print them in sorted order.

Examples:

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.
Input: arr[] = [3, 1, 2] 
Output: []
Explanation: There is no repeating element in the array, so the output is empty.
Constraints:
1 ≤ n ≤ 10^6
1 ≤ arr[i] ≤ n
"""

from src.python.Array_duplicates import Solution
from tests.python.util import fill_list_with_range, fill_sorted_list_with_range

sol = Solution()

# Sanity tests scenarios
def test_sanity_scenarios():
    assert sol.findDuplicates([2,3,1,2,3]) == [2,3]
    assert sol.findDuplicates([3,1,2]) == []

# Array with only one value
def test_only_one_value():
    assert sol.findDuplicates([2]) == []
    assert sol.findDuplicates([1000000]) == []

# Array with maimum elements possible 
def test_with_max_elements():
    array_nums = fill_list_with_range(1000000, 500000)
    result = fill_sorted_list_with_range(500000,500000)
    assert sol.findDuplicates(array_nums) == result

# Without repeted values
def test_without_repeted_values():
    assert sol.findDuplicates([2,3,4,5,6,7,8,9]) == []
