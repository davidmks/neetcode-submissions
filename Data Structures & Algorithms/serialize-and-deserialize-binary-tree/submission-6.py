# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []

        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                output.append("null")
                return
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)
        return ",".join(output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        i = 0
        # you can use iter + next instead of the index

        def dfs() -> Optional[TreeNode]:
            nonlocal i
            val = vals[i]
            i += 1
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
