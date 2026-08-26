# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = None
        while head != None :
            temp = head
            head = head.next
            temp.next = end
            end = temp
        return end
