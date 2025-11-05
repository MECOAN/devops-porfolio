"""
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
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ arr.size() + 1
"""

class Solution:
    def missingNum(self, arr):
        arr.sort()
        initial_value = 0
        final_value = len(arr) - 1
        mid_point = final_value // 2
        while(True):
            #if(mid_point == 0)
            #    return (arr[final_value]-1)
            if(arr[initial_value] != (initial_value+1)):
                return initial_value+1
            elif(arr[final_value] != (final_value+2)):
                return final_value + 2
            elif((final_value - initial_value) == 1):
                return (arr[final_value]-1)
            elif(arr[mid_point] > (mid_point+1)): # Caso con error a la izquirda
                final_value = mid_point
            else: # Caso error a la derecha
                initial_value = mid_point
            mid_point = initial_value + ((final_value - initial_value) // 2)
