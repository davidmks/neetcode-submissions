class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, first - second)
        return -stones[0] if stones else 0

        # # max heap only available in python 14
        # heapq.heapify_max(stones)

        # while len(stones) > 1:
        #     first = heapq.heappop_max(stones)  # heaviest
        #     second = heapq.heappop_max(stones)  # second heaviest
        #     if first != second:
        #         heapq.heappush_max(stones, first - second)

        # return stones[0] if stones else 0
