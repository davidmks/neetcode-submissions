# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # divide and conquer
        if not lists:
            return None

        def _merge_two_lists(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(_merge_two_lists(list1, list2))
            lists = merged
        return lists[0]

        # # heap
        # heap = []
        # for i, head in enumerate(lists):
        #     if head:
        #         heapq.heappush(heap, (head.val, i, head))

        # dummy = ListNode()
        # tail = dummy

        # while heap:
        #     val, i, node = heapq.heappop(heap)
        #     tail.next = node
        #     tail = node
        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, i, node.next))

        # return dummy.next
