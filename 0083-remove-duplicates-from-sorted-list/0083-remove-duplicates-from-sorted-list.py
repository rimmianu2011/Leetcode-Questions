# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current_val = head

        if not head:
            return None

        while current_val.next:

            if current_val.val == current_val.next.val:
                current_val.next = current_val.next.next
            
            else:
                current_val = current_val.next
            # print(current_val.val)

        return head