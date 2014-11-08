
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head:
            return head


        root = head
        index = 1

        prev_m = None
        n_node = None

        rev_list_last = None
        rev_list = None

        while root:

            if index == m-1:
                prev_m = root

            elif index == n+1:
                n_node = root
                break

            elif index >= m:
                if not rev_list:
                    rev_list = ListNode(root.val)
                    rev_list_last = rev_list
                else:
                    tmp = ListNode(root.val)
                    tmp.next = rev_list
                    rev_list = tmp

            index += 1
            root = root.next

        if prev_m:
            prev_m.next = rev_list
        else:
            head = rev_list

        if n_node:
            rev_list_last.next = n_node

        return head



# l1 = None
# l1 = ListNode(0)
# l1.next = ListNode(2)
# l1.next.next = ListNode(10)


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)
# l2.next.next.next.next.next = ListNode(2)

s = Solution()
result = s.reverseBetween(l2, 1, 2)
while result:
    print(result.val, '->')
    result = result.next