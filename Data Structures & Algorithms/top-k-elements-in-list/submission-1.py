class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
        
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1

        # sorted_counts = sorted(counts, key=counts.get, reverse=True)

        # return sorted_counts[:k]
