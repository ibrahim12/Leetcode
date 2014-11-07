
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return l1

        result = ListNode(0)
        root = result
        while l1 and l2:
            if l1.val < l2.val:
                result.next = ListNode(l1.val)
                l1 = l1.next

            elif l1.val > l2.val:
                result.next = ListNode(l2.val)
                l2 = l2.next

            else:
                result.next = ListNode(l1.val)
                result.next.next = ListNode(l2.val)
                result = result.next
                l1 = l1.next
                l2 = l2.next

            result = result.next


        while l1:
            result.next = ListNode(l1.val)
            result = result.next
            l1 = l1.next

        while l2:
            result.next = ListNode(l2.val)
            result = result.next
            l2 = l2.next


        return root.next



# l1 = None
# l1 = ListNode(0)
# l1.next = ListNode(2)
# l1.next.next = ListNode(10)


l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(8)

s = Solution()
result = s.mergeTwoLists(l1,l2)
while result:
    print(result.val, '->')
    result = result.next