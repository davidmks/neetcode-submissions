class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
        
            total = 0
            for p in piles:
                total += math.ceil(p/mid)
        
            if total <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
