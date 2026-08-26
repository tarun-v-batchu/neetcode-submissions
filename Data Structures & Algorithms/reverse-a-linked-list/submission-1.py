# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None :
            return head
        
        node = head
        head = head.next
        node.next = None
        while head != None :
            temp = head.next
            head.next = node
            node = head
            head = temp
            
        
        return node
    
        
