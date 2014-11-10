# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):

        if not head:
            return None

        root1 = head
        root2 = head

        while root1 or root2:

            if not root1.next:
                return None

            if not root2.next or not root2.next.next:
                return None

            root1 = root1.next
            root2 = root2.next.next

            if root1 == root2:
                break

        if not root1 or not root2:
            return None

        root1 = head

        while root1 != root2:
            root1 = root1.next
            root2 = root2.next

        return root2


# l1 = None
# l1 = ListNode(0)
# l1.next = ListNode(2)
# l1.next.next = ListNode(10)


l2 = ListNode(1)
# l2.next = ListNode(4)
# l2.next.next = ListNode(3)
# l2.next.next.next = ListNode(2)
# l2.next.next.next.next = ListNode(5)
# cycle = l2.next.next.next.next
# l2.next.next.next.next.next = cycle

s = Solution()
result = s.detectCycle(l2)
print(result.val if result else 'no cycle')