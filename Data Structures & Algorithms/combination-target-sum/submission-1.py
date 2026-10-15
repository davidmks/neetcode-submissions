class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def dfs(i, total):
            if total == target:
                res.append(combo.copy())
                return
            if i == len(nums) or total > target:
                return
            # include nums[i], and stay at i so it can be picked again
            combo.append(nums[i])
            dfs(i, total + nums[i])
            # undo, then move past nums[i] for good
            combo.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res
