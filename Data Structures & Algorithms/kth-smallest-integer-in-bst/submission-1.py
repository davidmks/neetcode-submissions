# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None
        def inorder(node:Optional[TreeNode]):
            nonlocal count, k,result
            if not node:
                return
            inorder(node.left)
            count += 1
            if count == k:
                result = node.val
                return
            inorder(node.right)
        inorder(root)
        return result
        
        # count = 0
        # stack = []
        # node = root
        # while node or stack:
        #     while node:
        #         stack.append(node)
        #         node = node.left
            
        #     node = stack.pop()
        #     count += 1
        #     if count == k:
        #         return node.val
            
        #     node = node.right
        
        