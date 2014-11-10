# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):

        if not head:
            return head

        root = head
        prev = None
        while root and root.next:

            if not prev:
                a = root
                b = root.next

                a.next = b.next
                b.next = a
                head = b
                root = root.next
                prev = a

            else:
                prev.next = root.next
                t = root.next.next
                root.next.next = root
                root.next = t
                prev = root

                root = root.next

        return head


# l1 = None
# l1 = ListNode(0)
# l1.next = ListNode(2)
# l1.next.next = ListNode(10)


l2 = ListNode(1)
l2.next = ListNode(4)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(2)
l2.next.next.next.next = ListNode(5)
# cycle = l2.next.next.next.next
# l2.next.next.next.next.next = cycle

s = Solution()
result = s.swapPairs(l2)
while result:
    print(result.val, '->')
    result = result.next