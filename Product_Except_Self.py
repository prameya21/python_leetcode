from typing import List
'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)==0:
            return []
        ret=[0]*len(nums)
        left,right=1,1
        for i in range(len(nums)):
            ret[i]=left
            left=left*nums[i]
        for i in range(len(nums)-1,-1,-1):
            ret[i]=ret[i]*right
            right=right*nums[i]
        return ret


obj=Solution()
print(obj.productExceptSelf([1,2,3,4]))