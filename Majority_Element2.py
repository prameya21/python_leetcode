from typing import List
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1,count2,candidate1,candidate2=0,0,0,1
        for i in nums:
            if i==candidate1:
                count1+=1
            elif i==candidate2:
                count2+=1
            elif count1==0:
                count1,candidate1=1,i
            elif count2==0:
                count2,candidate2=1,i
            else:
                count1,count2=count1-1,count2-1
        return [n for n in (candidate1,candidate2) if nums.count(n) > len(nums) // 3]


obj=Solution()
print(obj.majorityElement([1,1,1,3,3,2,2,2]))
num=[1,1,1,3,3,2,2,2]
print(len(num)//3)
