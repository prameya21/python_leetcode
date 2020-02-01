from typing import List

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return []
        map_indices={}
        for index,number in enumerate(nums):
            if (target-number) in map_indices:
                return [map_indices[target-number],index]
            map_indices[number]=index

obj=Solution()
print(obj.twoSum([2,7,11,15],9))