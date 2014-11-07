# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not n and not head:
            return head

        # if n == 1 and not head.next:
        #     return None

        root1 = head
        root2 = head


        while n:
            n -= 1
            root2 = root2.next

        if not root2:
            head = head.next
            return head

        prev = root1
        while root2:
            root2 = root2.next
            prev = root1
            root1 = root1.next

        prev.next = root1.next

        return head



l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(5)


s = Solution()
result = s.removeNthFromEnd(l1,1)
while result:
    print(result.val, '->')
    result = result.next