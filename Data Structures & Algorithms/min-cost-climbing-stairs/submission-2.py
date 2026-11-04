class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = 0, 0
        for i in range(2, len(cost) + 1):
            prev2, prev1 = prev1, min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        return prev1

        # memo = {}

        # def f(i: int) -> int:
        #     if i == 0:
        #         return 0
        #     if i == 1:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = min(f(i - 1) + cost[i - 1], f(i - 2) + cost[i - 2])
        #     return memo[i]

        # return f(len(cost))
