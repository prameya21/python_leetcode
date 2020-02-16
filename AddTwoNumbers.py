from ListNode import ListNode
from PrintList import list_print
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helper(l1,l2,0)

    def helper(self,l1,l2,carry):
        if l1 is None and l2 is None and carry == 0:
            return None
        sum=0
        sum+=l1.val if l1 is not None else 0
        sum+=l2.val if l2 is not None else 0
        sum+=carry
        head=ListNode(sum%10)
        head.next=self.helper(None if l1 is None else l1.next,None if l2 is None else l2.next,int(sum/10))
        return head



h1=ListNode(2)
h1.next=ListNode(4)
h1.next.next=ListNode(3)

h2=ListNode(5)
h2.next=ListNode(6)
h2.next.next=ListNode(4)

sol=Solution()
h3=sol.addTwoNumbers(h1,h2)

list_print(h3)
