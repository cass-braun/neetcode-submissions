# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        c1 = list1
        c2 = list2
        root = None
        if c1.val <= c2.val:
            root = c1
            c1 = c1.next
        else:
            root = c2
            c2 = c2.next

        curr = root
        while c1 and c2:
            if c1.val <= c2.val:
                curr.next = c1
                c1 = c1.next
                curr = curr.next

            else:
                curr.next = c2
                c2 = c2.next
                curr = curr.next
        
        if c1:
            curr.next = c1
        if c2:
            curr.next = c2
        
        return root
            
