'''

BruteForce - Make a list of all subsets and calculate the product and add them.
Optimal - Use the mathematical formula - [a,b](2 numbers in array) -> (1+a)(1+b) - 1
[a,b,c](3 numbers in array) -> (1+a)(1+b)(1+c) - 1, so on...
time - O(N)
space - O(1)
'''
class Solution:
    def subsetProductSum(self, arr):
        retVal = 1
        for i in range(len(arr)):
            retVal = retVal * (1+arr[i])
        return retVal - 1;

sol = Solution()
print(sol.subsetProductSum([1,2,3,4,5]))