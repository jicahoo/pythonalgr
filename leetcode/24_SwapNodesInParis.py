#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        mock_node = ListNode(0)
        b = mock_node
        p = head
        q = head.next
        if q is None:
            return head
        while p is not None and q is not None:
            # Exchange
            p.next = q.next
            b.next = q
            q.next = p

            # Update
            b = p
            p = p.next
            if p is not None:
                q = p.next
        return mock_node.next


def print_linked_list(head):
    p = head
    while p is not None:
        print p.val
        p = p.next

if __name__ == '__main__':
    s = Solution()
    #1->2->3->4
    head = ListNode(1)
    p = ListNode(2)
    head.next = p
    q = ListNode(3)
    p.next = q
    p = ListNode(4)
    q.next = p

    print_linked_list(head)
    head = s.swapPairs(head)
    print_linked_list(head)

    print s.swapPairs(None)

    head = ListNode(1)
    head = s.swapPairs(head)
    print_linked_list(head)

    head.next = ListNode(2)
    head.next.next = ListNode(4)
    head = s.swapPairs(head)
    print_linked_list(head)












