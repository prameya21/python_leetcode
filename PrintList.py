import ListNode

def list_print(head):
    while head is not None:
        print(head.val)
        head=head.next

head=ListNode.ListNode(5)
head.next=ListNode.ListNode(4)
head.next.next=ListNode.ListNode(3)
head.next.next.next=ListNode.ListNode(2)
head.next.next.next.next=ListNode.ListNode(1)

#list_print(head)


