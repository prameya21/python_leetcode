from typing import List
'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        res=[]
        nums.sort()
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k,l=j+1,len(nums)-1
                while k<l:
                    s=nums[i]+nums[j]+nums[k]+nums[l]
                    if s==target:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                    if s<=target:
                        k+=1
                        while nums[k]==nums[k-1] and k<l:
                            k+=1
                    if s>=target:
                        l-=1
                        while nums[l+1]==nums[l] and k<l:
                            l-=1
        return res


obj=Solution()
print(obj.fourSum([1,0,-1,0,-2,2],0))