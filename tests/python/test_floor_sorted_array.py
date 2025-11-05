"""
Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x. This element is called the floor of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of ceil of x, return the index of the last occurrence.

Examples

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 5
Output: 1
Explanation: Largest number less than or equal to 5 is 2, whose index is 1.
Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 11
Output: 4
Explanation: Largest Number less than or equal to 11 is 10, whose indices are 3 and 4. The index of last occurrence is 4.
Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 0
Output: -1
Explanation: No element less than or equal to 0 is found. So, output is -1.
Constraints:
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^6
0 ≤ x ≤ arr[n-1]
"""


from src.python.Floor_in_a_sorted_array import Solution
from tests.python.util import fill_list_with_range

sol = Solution()

def test_sanity_scenarios():
    assert sol.findFloor([1,2,8,10,10,12,19], 5) == 1
    assert sol.findFloor([1,2,8,10,10,12,19], 11) == 4

# Scenarios with one value in the array
def test_one_value_array():
    assert sol.findFloor([5], 6) == 0
    assert sol.findFloor([1], 999999) == 0

# Scenarios with 10^6 values in the array
def test_array_max_values():
    assert sol.findFloor(fill_list_with_range(1000000,1000000), 900000) == 899999
    sorted_list = fill_list_with_range(1000000,384624,123)
    sorted_list.sort()
    assert sol.findFloor(sorted_list, 293437) == 817625

# Scenarios without the floor of x
def test_with_missing_floor():
    sorted_list = fill_list_with_range(1000000,384624,123)
    sorted_list.sort()
    assert sol.findFloor(sorted_list, 120) == -1
    assert sol.findFloor([1,2,8,10,10,12,19], 0) == -1
    assert sol.findFloor([5], 2) == -1

# Scenarios with the floor at the begin
def test_floor_in_the_first_field():
    assert sol.findFloor([4], 5) == 0
    assert sol.findFloor([1,3,4,6,7,9], 2) == 0
    sorted_list = fill_list_with_range(1000000,1000000)
    sorted_list.sort()
    assert sol.findFloor(sorted_list, 1) == 0

# Scenarios with the floor at the end
def test_floor_at_the_end():
    assert sol.findFloor([10,35], 36) == 1
    assert sol.findFloor([1,1,1,1,2,3,4,5,6,7,7,8,9,10,10,12,13,14,15,15,16,17,18,19,19,20,21,21,22,23,23], 23) == 30
    sorted_list = fill_list_with_range(1000000,200,50)
    sorted_list.sort()
    assert sol.findFloor(sorted_list, 201) == 999999


# Scenarios with the array full with the same value
def test_array_with_same_value():
    assert sol.findFloor([1,1,1,1,1], 2) == 4
    sorted_list = fill_list_with_range(1000000,200,200)
    sorted_list.sort()
    assert sol.findFloor(sorted_list, 201) == 999999
