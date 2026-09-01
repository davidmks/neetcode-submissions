class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 1. solution (sliding window)
        left = 0
        total = 0
        best = float("inf")
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if best == float("inf") else best

        # 2. solution (binary search)
        # TODO when i get to this chapter
