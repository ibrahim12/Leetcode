
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def partition(self, head, x):
        if not head:
            return  head


        root = head
        prev = None

        root_s = ListNode(0)
        head_s = root_s

        while root:
            if root.val < x :

                if not prev:
                    head = head.next
                else:
                    prev.next = root.next

                root_s.next = ListNode(root.val)
                root_s = root_s.next

            else:
                prev = root

            root = root.next

        head_s = head_s.next

        if not head:
            return head_s

        if not head_s:
            return head

        root_s.next = head
        return head_s









# l1 = None
# l1 = ListNode(0)
# l1.next = ListNode(2)
# l1.next.next = ListNode(10)


l2 = ListNode(1)
l2.next = ListNode(4)
# l2.next.next = ListNode(3)
# l2.next.next.next = ListNode(2)
# l2.next.next.next.next = ListNode(5)
# l2.next.next.next.next.next = ListNode(2)

s = Solution()
result = s.partition(l2, 5)
while result:
    print(result.val, '->')
    result = result.next