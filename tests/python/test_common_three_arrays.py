"""
Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. If there are no such elements return an empty array. In this case, the output will be -1.

Note: can you handle the duplicates without using any additional Data Structure?

Examples :

Input: arr1 = [1, 5, 10, 20, 40, 80] , arr2 = [6, 7, 20, 80, 100] , arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output: [20, 80]
Explanation: 20 and 80 are the only common elements in arr1, arr2 and arr3.
Input: arr1 = [1, 2, 3, 4, 5] , arr2 = [6, 7] , arr3 = [8,9,10]
Output: [-1]
Explanation: There are no common elements in arr1, arr2 and arr3.
Input: arr1 = [1, 1, 1, 2, 2, 2], arr2 = [1, 1, 2, 2, 2], arr3 = [1, 1, 1, 1, 2, 2, 2, 2]
Output: [1, 2]
Explanation: We do not need to consider duplicates
Constraints:
1 <= arr1.size(), arr2.size(), arr3.size() <= 10^5
-10^5 <= arr1i , arr2i , 1arr3i <= 10^5
"""

from src.python.Common_in_three_sorted_arrays import Solution
from tests.python.util import fill_sorted_list_with_range

sol = Solution()

# Sanity tests scenarios
def test_sanity_scenarios():
    arr1 = [1,5,10,20,40,80]
    arr2 = [6,7,20,80,100]
    arr3 = [3,4,15,20,30,70,80,120]
    solution = [20,80]
    assert sol.commonElements(arr1, arr2, arr3) == solution
    arr1 = [1,1,1,2,2,2]
    arr2 = [1,1,2,2,2]
    arr3 = [1,1,1,1,2,2,2,2]
    solution = [1,2]
    assert sol.commonElements(arr1, arr2, arr3) == solution

# Scenarios with one element array
def test_one_element_array_scenarios():
    assert sol.commonElements([1], [1], [1]) == [1]
    assert sol.commonElements([-99999], [-99999], [-99999]) == [-99999]

# Scenarios with very big arrays
def test_very_big_arrays():
    arr1 = fill_sorted_list_with_range(100000, 10, 5)
    arr2 = fill_sorted_list_with_range(100000, 100000)
    arr3 = fill_sorted_list_with_range(100000, 200000,3)
    solution = [5,6,7,8,9,10]
    assert sol.commonElements(arr1, arr2, arr3) == solution
    arr1 = fill_sorted_list_with_range(100000, 10, -10)
    arr2 = fill_sorted_list_with_range(100000, 10000, -10000)
    arr3 = fill_sorted_list_with_range(100000, 5, -5)
    solution = [-5,-4,-3,-2,-1,0,1,2,3,4,5]

# Only negative values
def test_only_negative_values():
    arr1 = [-9,-8,-7,-6,-5,-4,-3,-2,-1]
    arr2 = fill_sorted_list_with_range(100000, -1, -10)
    arr3 = [-8,-6,-4,-2]
    solution = [-8,-6,-4,-2]
    assert sol.commonElements(arr1,arr2,arr3) == solution
    arr1 = fill_sorted_list_with_range(100000, -1, -10)
    arr2 = fill_sorted_list_with_range(100000, -15, -100)
    arr3 = fill_sorted_list_with_range(100000, -1000, -15000)
    solution = [-1]
    assert sol.commonElements(arr1,arr2,arr3) == solution

# Any value match
def test_any_value_match():
    arr1 = [1,2,3,4,5]
    arr2 = [6,7]
    arr3 = [8,9,10]
    solution = [-1]
    assert sol.commonElements(arr1, arr2, arr3) == solution

# All the values matches
    arr1 = [1,1,1,1,1,1,2,2,2,2,2,3,4,4,4,4,5,6,7,7,7,7,8,8,8,8,8,8]
    arr2 = [1,2,3,4,5,6,7,8]
    arr3 = [1,2,3,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,7,7,7,7,8]
    solution = [1,2,3,4,5,6,7,8]
    assert sol.commonElements(arr1, arr2, arr3) == solution
    arr1 = fill_sorted_list_with_range(100000,100,-100)
    arr2 = fill_sorted_list_with_range(100000,100,-100)
    arr3 = fill_sorted_list_with_range(100000,100,-100)
    solution = fill_sorted_list_with_range(201,100,-100)
    assert sol.commonElements(arr1,arr2,arr3) == solution
