# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        inorder_index_of = {v: k for k, v in enumerate(inorder)}

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left > right:
                return None
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)
            
            mid = inorder_index_of[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)

        # # with slicing O(n^2)
        # if not preorder:
        #     return None
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        # return root
