"""
Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

Examples:

Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, 1]]
Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
arr[2] + arr[4] = 1 + (-1) = 0.
The distinct pair are [-1,1].
Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
Output: [[-6, 6],[-1, 1]]
Explanation: The distinct pairs are [-1, 1] and [-6, 6].
Expected Time Complexity: O(n log n)
Expected Auxiliary Space: O(n).

Constraints:
3 <= arr.size <= 10^5
-10^5 <= arr[i] <= 10^5
"""

from src.python.Two_sum_pairs_with_cero_sum import Solution
from tests.python.util import fill_sorted_list_with_range, fill_list_with_range, fill_array_of_arrys

sol = Solution()

# Sanity tests scenarios
def test_sanity_scenarios():
    assert sol.getPairs([-1,0,1,2,-1,-4]) == [[-1,1]]
    assert sol.getPairs([6,1,8,0,4,-9,-1,-10,-6,-5]) == [[-6,6],[-1,1]]

# Array with only three elements
def test_small_array_scenarios():
    assert sol.getPairs([-1,0,1]) == [[-1,1]]
    assert sol.getPairs([-100000,-99999,100000]) == [[-100000,100000]]

# Array with the maximum elements allowed
def test_maximum_allowed_elements():
    list_t = fill_sorted_list_with_range(100000, 50, -5)
    solution = fill_array_of_arrys(5)
    assert sol.getPairs(list_t) == solution
    list_t = fill_sorted_list_with_range(100000, 10000, -5000)
    solution = fill_array_of_arrys(5000)
    assert sol.getPairs(list_t) == solution

# All values are pairs
def test_all_values_match():
    list_t = fill_sorted_list_with_range(50, 25, -25)
    solution = fill_array_of_arrys(24)
    solution.remove([0,0])
    assert sol.getPairs(list_t) == solution
    list_t = fill_sorted_list_with_range(100000, 50000, -50000)
    solution = fill_array_of_arrys(49999)
    solution.remove([0,0])
    assert sol.getPairs(list_t) == solution

# Full with zero
def test_all_values_zero():
    list_t = fill_sorted_list_with_range(50, 0)
    assert sol.getPairs(list_t) == [[0,0]]
    list_t = fill_sorted_list_with_range(100000, 0)
    assert sol.getPairs(list_t) == [[0,0]]
