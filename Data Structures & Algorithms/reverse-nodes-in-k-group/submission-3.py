# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def _get_kth(curr: Node, k: int) -> Node:
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, next=head)
        group_prev = dummy

        while True:
            kth = _get_kth(group_prev, k)
            if kth is None:
                break
            group_next = kth.next

            # reverse
            prev, curr = group_next, group_prev.next
            while curr is not group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            new_tail = group_prev.next
            group_prev.next = kth
            group_prev = new_tail
        
        return dummy.next
