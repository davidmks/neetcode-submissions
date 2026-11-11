class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        n = len(nums)
        memo = {}

        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i == n:
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i, target)] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            return memo[(i, target)]

        return dfs(0, total // 2)
