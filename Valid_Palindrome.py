'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

class Solution:
    def isPalindrome(self,s:str) -> bool:
        s=s.lower()
        l,r=0,len(s)-1
        while l<=r:
            if not s[l].isdigit() and not s[l].isalpha():
                l+=1
            elif not s[r].isdigit() and not s[r].isalpha():
                r-=1
            else:
                if s[l]!=s[r]:
                    return False
                l+=1;r-=1
        return True




obj=Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))