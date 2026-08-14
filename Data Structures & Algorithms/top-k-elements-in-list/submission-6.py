class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 3. solution (buckets)
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        res = []
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res

        # ---

        ## 2. solution (hash counts - head)
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1

        # heap = []
        # for num, freq in counts.items():
        #     heapq.heappush(heap, (freq, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [num for _, num in heap]

        # ---

        ## 1. solution (hash counts - sort)
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1

        # sorted_counts = sorted(counts, key=counts.get, reverse=True)

        # return sorted_counts[:k]
