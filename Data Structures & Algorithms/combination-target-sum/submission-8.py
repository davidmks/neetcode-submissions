class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def backtrack(start, total):
            if total == target:
                res.append(combo.copy())
                return
            for i in range(start, len(nums)):
                if nums[i] + total > target:
                    continue
                combo.append(nums[i])
                backtrack(i, nums[i] + total)
                combo.pop()

        backtrack(0,0)
        return res
