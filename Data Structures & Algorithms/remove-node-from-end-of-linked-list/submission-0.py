# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length, node = 0, head
        while node != None :
            length += 1
            node = node.next
        
        removal = length - n
        
        if removal == 0:
            return head.next
        
        i, node = 0, head
        while i < removal - 1:
            # print(node.val, removal)
            node = node.next
            i += 1
        
        node.next = node.next.next
        return head