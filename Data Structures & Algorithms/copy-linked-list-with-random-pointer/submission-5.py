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
        copies = {None: None}

        node = head
        while node:
            copies[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            copies[node].next = copies[node.next]
            copies[node].random = copies[node.random]
            node = node.next

        return copies[head]

        # if not head:
        #     return None

        # # A -> A' -> B -> B' -> C -> C'
        # node = head
        # while node:
        #     copy = Node(node.val)
        #     next_node = node.next
        #     node.next = copy
        #     copy.next = next_node
        #     node = next_node

        # node = head
        # while node:
        #     if node.random:
        #         node.next.random = node.random.next
        #     node = node.next.next

        # node = head
        # new_head = node.next
        # while node:
        #     copy = node.next
        #     node.next = copy.next
        #     copy.next = copy.next.next if copy.next else None
        #     node = node.next

        # return new_head
