# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False

        rsum = sum - root.val

        if rsum == 0 and ( root.left == None and root.right == None):
            return True

        return self.hasPathSum(root.left, rsum) or self.hasPathSum(root.right, rsum)



root = TreeNode(1)
root.left = TreeNode(-2)
root.left.left = TreeNode(-3)
root.left.left.left = TreeNode(-2)
root.left.right = TreeNode(1)
root.right = TreeNode(-3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)

# root.right = TreeNode(-1)
# root.right.left = TreeNode(13)
# root.right.left = TreeNode(4)
# root.right.left.left = TreeNode(1)

s = Solution()
print(s.hasPathSum(root, -1))