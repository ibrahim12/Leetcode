import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head:
            return head

        if not head.next:
            return head

        root = head
        reverse = ListNode(root.val)
        root = root.next
        count = 1
        while root:

            tmp = ListNode(root.val)
            tmp.next = reverse
            reverse = tmp

            root = root.next
            count += 1


        root = head
        l_count = count // 2

        while l_count:
            l_count -= 1

            tmp = root.next
            root.next = ListNode(reverse.val)
            root.next.next = tmp

            if l_count:
                root = root.next.next
            else:
                root = root.next

            reverse = reverse.next

        if count % 2:
            root.next.next = None
        else:
            root.next = None

        return head


# l1 = None
# l1 = ListNode(0)
# l1.next = ListNode(2)
# l1.next.next = ListNode(10)

# l2 = None

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
# l2.next.next.next = ListNode(4)
# l2.next.next.next.next = ListNode(5)
# l2.next.next.next.next.next = ListNode(2)

s = Solution()
result = s.reorderList(l2)
while result:
    print(result.val, '->')
    result = result.next