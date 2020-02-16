'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l,r,maxCount=0,0,0
        while l<len(s) and r<len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                maxCount=max(maxCount,r-l+1)
                r+=1
            else:
                charSet.remove(s[l])
                l+=1;
        return maxCount



obj=Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))
print(obj.lengthOfLongestSubstring('pwwkew'))