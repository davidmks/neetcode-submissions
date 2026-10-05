# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]):
            if not node:
                return True, 0
            left_ok, left = height(node.left)
            right_ok, right = height(node.right)
            balanced = left_ok and right_ok and abs(left - right) <= 1
            return balanced, 1 + max(left, right)

        ok, _ = height(root)
        return ok
