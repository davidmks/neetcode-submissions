class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. solution (greedy)
        best = 0
        min_price = prices[0]
        for price in prices[1:]:
            best = max(best, price - min_price)
            min_price = min(min_price, price)
        return best
        
        # # 2. solution (sliding window)
        # left, right = 0, 1
        # best = 0
        # while right < len(prices):
        #     if prices[left] < prices[right]:
        #         best = max(best, prices[right] - prices[left])
        #     else:
        #         left = right
        #     right += 1
        # return best


