# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def prnt(curr: ListNode):
    while curr:
        print(curr.val)
        curr = curr.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        
        return dummy.next
            

            
            
