class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(i: int) -> int:
            if i == 0:
                return 1
            if i == 1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = climb(i - 1) + climb(i - 2)
            return memo[i]

        return climb(n)
