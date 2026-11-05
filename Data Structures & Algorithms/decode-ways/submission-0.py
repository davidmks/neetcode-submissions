class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def ways(i: int) -> int:
            if i < 0:
                return 1
            if i in memo:
                return memo[i]
            one_digit = ways(i - 1) if s[i] != "0" else 0
            two_digit = ways(i - 2) if i >= 1 and 10 <= int(s[i - 1 : i + 1]) <= 26 else 0
            memo[i] = one_digit + two_digit
            return memo[i]

        return ways(len(s) - 1)
