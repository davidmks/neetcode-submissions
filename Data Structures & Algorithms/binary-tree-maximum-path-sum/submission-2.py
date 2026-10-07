# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val

        def gain(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0

            left = gain(node.left)
            right = gain(node.right)

            left = max(left, 0)
            right = max(right, 0)

            # best path with this node as its top (may use both sides - split)
            best = max(best, node.val + left + right)

            # best downward chain from this node (one side only - no split), for the parent to extend
            return node.val + max(left, right)

        gain(root)
        return best
