
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):

        if not l1 and not l2:
            return ListNode(0)

        result = ListNode(0)
        root = result
        rem = 0
        while l1 or l2 or rem:
            val = rem

            if l1:
                val += l1.val
                l1 = l1.next

            if l2:
                val += l2.val
                l2 = l2.next

            rem = 1 if val >= 10 else 0
            val =  val % 10

            # print(val, rem)
            result.next = ListNode(val)
            result = result.next

        return root.next


l1 = ListNode(0)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)


l2 = ListNode(0)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

s = Solution()
result = s.addTwoNumbers(l1,l2)
while result:
    print(result.val, '->')
    result = result.next