class Solution:
    def climbStairs(self, n: int) -> int:
        prev2, prev1 = 1, 1

        for i in range(2, n + 1):
            prev2, prev1 = prev1, prev1 + prev2

        return prev1

        # memo = {}
        # def climb(i: int) -> int:
        #     if i == 0:
        #         return 1
        #     if i == 1:
        #         return 1
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = climb(i - 1) + climb(i - 2)
        #     return memo[i]

        # return climb(n)
