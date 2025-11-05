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


class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i1 = 0
        i2 = 0
        i3 = 0
        result = []
        
        while(i1 < len(arr1) and i2 < len(arr2) and i3 < len(arr3)):
            val1 = arr1[i1]
            val2 = arr2[i2]
            val3 = arr3[i3]
            if(val1 == val2 and val2 == val3):
                if not(len(result) != 0 and val1 in result):
                    result.append(val1)
                i1+=1
                i2+=1
                i3+=1
            elif(val1 < val2):
                i1+=1
            elif(val2 < val3):
                i2+=1
            else:
                i3+=1
                
            while(i1 > 0 and i1 < len(arr1) and arr1[i1] == arr1[i1-1]):
                i1+=1
            while(i2 > 0 and i2 < len(arr2) and arr2[i2] == arr2[i2-1]):
                i2+=1
            while(i3 > 0 and i3 < len(arr3) and arr3[i3] == arr3[i3-1]):
                i3+=1
        if(len(result) == 0):
            result.append(-1)
        return result
