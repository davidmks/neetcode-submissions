class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2
            hours = sum(math.ceil(pile / k) for pile in piles)

            if hours <= h:
                result = k
                right = k - 1
            else:
                left = k + 1

        return result
