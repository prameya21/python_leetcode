from typing import List
'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return 0
        ret=sum(nums[:3])
        nums.sort()
        for i in range(len(nums)-2):
            j,k=i+1,len(nums)-1
            s=nums[i]+nums[j]+nums[k]
            if abs(s-target)<abs(ret-target):
                ret=s
            if s<target:
                j+=1
            elif s>target:
                k-=1
        return ret



obj=Solution()
print(obj.threeSumClosest([-1,2,1,-4],1))