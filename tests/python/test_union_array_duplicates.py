"""
You are given two arrays a[] and b[], return the Union of both the arrays in any order.

The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

Note: Elements of a[] and b[] are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result in sorted order only.

Examples:

Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
Output: [1, 2, 3]
Explanation: Union set of both the arrays will be 1, 2 and 3.
Input: a[] = [1, 2, 3], b[] = [4, 5, 6] 
Output: [1, 2, 3, 4, 5, 6]
Explanation: Union set of both the arrays will be 1, 2, 3, 4, 5 and 6.
Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
Output: [1, 2]
Explanation: Union set of both the arrays will be 1 and 2.
Constraints:
1 ≤ a.size(), b.size() ≤ 10^6
0 ≤ a[i], b[i] ≤ 10^5
"""

from src.python.Union_of_arrays_with_duplicates import Solution
from tests.python.util import fill_list_with_range

sol = Solution()

# Sanity test
def test_sanity_scenarios():
    assert sol.findUnion([1,2,3,2,1],[3,2,2,3,3,2]) == {1,2,3}
    assert sol.findUnion([1,2,3],[4,5,6]) == {1,2,3,4,5,6}
    assert sol.findUnion([1,2,1,1,2],[2,2,1,2,1]) == {1,2}

# Arrays with only one value
def test_small_arrays():
    assert sol.findUnion([1],[2]) == {1,2}
    assert sol.findUnion([100000],[20000]) == {20000,100000}
    assert sol.findUnion([50],[500]) == {50,500}
    assert sol.findUnion([500],[5001]) == {500,5001}

# Arrays with 10^6 values
def test_big_arrays():
    first_array = fill_list_with_range(1000000,99999,50000)
    second_array = fill_list_with_range(1000000,100000,50)
    result = set(first_array) | set(second_array)
    assert sol.findUnion(list(first_array),list(second_array)) == result
    first_array = fill_list_with_range(1000000, 10000)
    second_array = fill_list_with_range(1000000, 50000, 15000)
    result = set(first_array) | set(second_array)
    assert sol.findUnion(first_array, second_array) == result


# Both arrays with same values
def test_same_lists():
    assert sol.findUnion([1,2,3],[1,2,3]) == {1,2,3}
    assert sol.findUnion([2,6,4,8,7,3,1,0,7,5,4,3,8,7,0,5,4,8,7,3,2],[2,6,4,8,7,3,1,0,7,5,4,3,8,7,0,5,4,8,7,3,2]) == {0,1,2,3,4,5,6,7,8}
    assert sol.findUnion([1],[1]) == {1}
    first_array = fill_list_with_range(1000000,100000)
    second_array = fill_list_with_range(1000000,100000)
    result = set(first_array) | set(second_array)
    assert sol.findUnion(first_array, second_array) == result

# Both arrays with differents values
def test_both_lists_different():
    assert sol.findUnion([1,2,3,4],[9,8,7,6]) == {1,2,3,4,6,7,8,9}
    assert sol.findUnion([1,6,4,8,7,6,4,5,6,1,2,3,4,5,8,7,9],[15,18,20,13,11,14,12,14,13,20,19,17,18]) == {1,2,3,4,5,6,7,8,9,11,12,13,14,15,17,18,19,20}
    first_array = fill_list_with_range(1000000,10000)
    second_array = fill_list_with_range(1000000,50000,30000)
    result = set(first_array) | set(second_array)
    assert sol.findUnion(first_array, second_array) == result

