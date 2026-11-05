class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def fewest(a):
            if a < 0:
                return float("inf")
            if a == 0:
                return 0
            if a in memo:
                return memo[a]
            memo[a] = 1 + min(fewest(a - c) for c in coins)
            return memo[a]

        res = fewest(amount)
        return res if res != float("inf") else -1
