class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hi = lo = res = nums[0]
        for n in nums[1:]:
            candidates = (n, n * hi, n * lo)
            hi, lo = max(candidates), min(candidates)
            res = max(res, hi)
        return res
