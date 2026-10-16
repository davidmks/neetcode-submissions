class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def backtrack(start, total):
            if total == target:
                res.append(combo.copy())
                return
            for i in range(start, len(nums)):
                if total > target:
                    continue
                combo.append(nums[i])
                backtrack(i, total + nums[i])
                combo.pop()

        backtrack(0, 0)
        return res
