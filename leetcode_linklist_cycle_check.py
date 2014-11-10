# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):

        if not head:
            return False

        root1 = head
        root2 = head

        while root1 or root2:

            if not root1.next:
                return False

            if not root2.next or not root2.next.next:
                return False

            root1 = root1.next
            root2 = root2.next.next

            if root1 == root2:
                return True

        return False




# l1 = None
# l1 = ListNode(0)
# l1.next = ListNode(2)
# l1.next.next = ListNode(10)


l2 = ListNode(1)
l2.next = ListNode(4)
cycle = l2.next.next = ListNode(3)
l2.next.next.next = ListNode(2)
l2.next.next.next.next = ListNode(1)
l2.next.next.next.next.next = cycle

s = Solution()
result = s.hasCycle(l2)
print(result)