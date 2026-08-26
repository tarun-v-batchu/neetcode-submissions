# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(((l1.val if l1 != None else 0) + (l2.val if l2 != None else 0)) % 10)
        ret = head
        carry = ((l1.val if l1 != None else 0) + (l2.val if l2 != None else 0)) // 10
        
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None

        while l1 != None or l2 != None :
            val = ((l1.val if l1 != None else 0) + (l2.val if l2 != None else 0)) + carry
            dig = val % 10
            carry = val // 10
            head.next = ListNode(dig)
            l1, l2, head = l1.next if l1 != None else None, l2.next if l2 != None else None, head.next
    
        if carry > 0 :
            head.next = ListNode(carry)
        
        return ret

