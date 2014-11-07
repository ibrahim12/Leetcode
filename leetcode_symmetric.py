# Definition for a  binary tree node
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     # @param root, a tree node
#     # @return a boolean
#     def isSymmetric(self, root):
#
#         if root == None:
#             return True
#
#         if not root.left and not root.right:
#             return True
#
#         if root.left and root.right and root.left.val == root.right.val:
#             return ( self.isSymmetric(root.left) and self.isSymmetric(root.right))
#         else:
#             return False

# class Solution:
#     # @param root, a tree node
#     # @return a boolean
#
#     def isSymmetric(self, root):
#
#         if root == None:
#             return True
#
#         if not root.left and not root.right:
#             return True
#
#         stack = [root.left, root.right]
#
#         while( len(stack) ):
#
#             front = stack.pop()
#             back = stack.pop()
#
#             if not front and not back:
#                 continue
#
#             if not front or not back and front != back:
#                 return False
#
#             if front.val != back.val:
#                 return False
#
#             stack.append(front.left)
#             stack.append(back.right)
#
#             stack.append(front.right)
#             stack.append(back.left)
#
#         return True


class Solution:
    # @param root, a tree node
    # @return a boolean

    def _check(self, left, right):
        if not left or not right:
            return left == right

        return (left.val == right.val) and self._check(left.left, right.right) and self._check(left.right, right.left)

    def isSymmetric(self, root):

        if root == None:
            return True

        return self._check(root.left, root.right)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)

s = Solution()
print(s.isSymmetric(root))