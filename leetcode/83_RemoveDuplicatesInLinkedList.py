# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Beat 81.72%
        # Try to analyze and resolve the problem from the problem itself, not the common way resolved similar problem.
        # For the clean logic, try to use uniform expression for the initial status and intermediate processing.
        # The key here is to use a variable
        # to store the info pointing to the last node which has the same value with
        # the current node's.
        current = head
        while current is not None:
            # Find current duplicate nods if any.
            last_node_with_same_value = current
            while (last_node_with_same_value.next is not None) and (last_node_with_same_value.val == last_node_with_same_value.next.val):
                last_node_with_same_value = last_node_with_same_value.next
            if last_node_with_same_value == current:
                current = current.next
            else:
                current.next = last_node_with_same_value.next
        return head







        return head