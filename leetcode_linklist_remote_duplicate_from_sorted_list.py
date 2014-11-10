
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
        current_val = head.val
        prev = head
        head = head.next
        while head:

            if head.val == current_val:
                prev.next = head.next
            else:
                prev = head

            current_val = head.val
            head = head.next

        return root



# l1 = None
# l1 = ListNode(0)
# l1.next = ListNode(2)
# l1.next.next = ListNode(10)


l2 = ListNode(1)
l2.next = ListNode(1)
# l2.next.next = ListNode(2)
# l2.next.next.next = ListNode(3)

s = Solution()
result = s.deleteDuplicates(l2)
while result:
    print(result.val, '->')
    result = result.next