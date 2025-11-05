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


class Solution:
    def getPairs(self, arr):
        s = set(arr)
        res = []
        
        if arr.count(0) > 1:
            res.append([0, 0])
        
        for x in s:
            if -x in s and x < 0:  # solo una vez por par
                res.append([x, -x])
        
        res.sort()          # O(k log k), k = número de pares
        return res
