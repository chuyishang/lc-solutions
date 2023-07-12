# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        head = ListNode(list1.val)
        p1 = head
        list1 = list1.next
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                p1.next = list1
                list1 = list1.next
            else:
                p1.next = list2
                list2 = list2.next
            p1 = p1.next
        if list1 is None:
            p1.next = list2
        else:
            p1.next = list1
        return head