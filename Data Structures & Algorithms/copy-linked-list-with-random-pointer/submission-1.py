"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return
        
        old_to_new = {}

        node = head
        while node:
            old_to_new[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            new = old_to_new[node]
            new.next = old_to_new.get(node.next)
            new.random = old_to_new.get(node.random)
            node = node.next

        return old_to_new[head]
