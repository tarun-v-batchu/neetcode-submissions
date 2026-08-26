# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None :
            return list1
        
        curr = None
        if list1.val < list2.val :
            curr = list1
            list1 = list1.next
            curr.next = None
        else :
            curr = list2
            list2 = list2.next
            curr.next = None
        head = curr
        while list1 != None and list2 != None :
            if list1.val < list2.val :
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                curr.next = None
            else :
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                curr.next = None
        if list1 == None :
            curr.next = list2
        else :
            curr.next = list1
        
        return head
