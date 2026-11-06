class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c > a:
                    continue
                dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != INF else -1

        # memo = {}

        # def fewest(a):
        #     if a < 0:
        #         return float("inf")
        #     if a == 0:
        #         return 0
        #     if a in memo:
        #         return memo[a]
        #     memo[a] = 1 + min(fewest(a - c) for c in coins)
        #     return memo[a]

        # res = fewest(amount)
        # return res if res != float("inf") else -1
