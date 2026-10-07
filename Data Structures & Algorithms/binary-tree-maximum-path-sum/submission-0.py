# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left = max(left, 0)
            right = max(right, 0)

            # compute the max path with a split
            best = max(best, node.val + left + right)

            # return the max path without a split
            return node.val + max(left, right)

        dfs(root)
        return best
