from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(i: int) -> int:
            if i == 0:
                return 1
            if i == 1:
                return 1
            return climb(i - 1) + climb(i - 2)

        return climb(n)
