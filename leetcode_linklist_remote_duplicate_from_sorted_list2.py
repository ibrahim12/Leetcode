
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head

        root = head
        prev = None
        while root and root.next:

            if not prev:
                if root.val == root.next.val:
                    while root.next and root.val == root.next.val:
                        root = root.next
                    head = root.next
                    root = head
                else:
                    prev = root
                    root = root.next

            else:

                if root.val == root.next.val:
                    while root.next and root.val == root.next.val:
                        root = root.next
                    prev.next = root.next
                    root = root.next
                else:
                    prev = root
                    root = root.next

        return head



# l1 = None
# l1 = ListNode(0)
# l1.next = ListNode(2)
# l1.next.next = ListNode(10)


l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(1)
l2.next.next.next = ListNode(1)
l2.next.next.next.next = ListNode(1)

s = Solution()
result = s.deleteDuplicates(l2)
while result:
    print(result.val, '->')
    result = result.next