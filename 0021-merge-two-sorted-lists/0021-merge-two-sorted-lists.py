# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = ListNode()
        new_sorted_list = new_list

        while list1 and list2:
            if list1.val < list2.val:
                new_sorted_list.next = list1
                list1 = list1.next
            else:
                new_sorted_list.next = list2
                list2 = list2.next

            new_sorted_list = new_sorted_list.next

        if list1:
            new_sorted_list.next = list1
        elif list2:
            new_sorted_list.next = list2

        return new_list.next
        