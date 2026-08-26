# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length, node = 0, head
        while node :
            length += 1
            node = node.next
        
        head = ListNode(-1, head)
        i, node = 0, head
        while i < length - n :
            node = node.next
            i += 1
        node.next = node.next.next
        return head.next