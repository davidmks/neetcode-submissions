class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def backtrack(start, total):
            if total == target:
                res.append(combo.copy())
            if start == len(nums) or total > target:
                return
            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(i, total + nums[i])
                combo.pop()

        backtrack(0, 0)
        return res
