"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        old_to_copy = {}

        def clone(original):
            if original in old_to_copy:
                return old_to_copy[original]

            copy = Node(original.val)
            old_to_copy[original] = copy

            for nei in original.neighbors:
                copy.neighbors.append(clone(nei))
            return copy

        return clone(node) if node else None
