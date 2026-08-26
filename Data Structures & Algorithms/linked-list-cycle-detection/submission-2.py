# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None :
            return False
        fast, slow = head.next.next, head.next
        while fast and slow and fast.val != slow.val:
            if fast.next == None :
                return False
            fast, slow = fast.next.next, slow.next
        
        if fast and slow and fast.val == slow.val :
            return True
        return False
            