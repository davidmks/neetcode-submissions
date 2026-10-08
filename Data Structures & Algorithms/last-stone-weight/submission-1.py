class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)
        
        while stones:
            if len(stones) < 2:
                return heapq.heappop_max(stones)
            stone_a = heapq.heappop_max(stones)
            stone_b = heapq.heappop_max(stones)
            stone = stone_a - stone_b
            if stone:
                heapq.heappush_max(stones,stone)
        return 0