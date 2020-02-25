from typing import List
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n=len(nums)
        n+=1
        sum=int((n*(n-1))/2)
        print(sum)
        for i in nums:
            sum=sum-i
        return sum


    def missingNumberXOR(self,nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing



obj=Solution()
print(obj.missingNumberXOR([9,6,4,2,3,5,7,0,1]))