class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 1. solution (sliding window)
        left = 0
        total = 0
        best = len(nums) + 1
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1
        return best if best <= len(nums) else 0

        # 2. solution (binary search)
        # TODO when i get to this chapter
