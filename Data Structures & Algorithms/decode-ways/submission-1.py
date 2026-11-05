class Solution:
    def numDecodings(self, s: str) -> int:
        two_back, one_back = 0, 1
        for i in range(len(s)):
            one_digit = one_back if s[i] != "0" else 0
            two_digit = two_back if i >= 1 and 10 <= int(s[i - 1 : i + 1]) <= 26 else 0
            two_back, one_back = one_back, one_digit + two_digit
        return one_back
        # memo = {}

        # def ways(i: int) -> int:
        #     if i < 0:
        #         return 1
        #     if i in memo:
        #         return memo[i]
        #     one_digit = ways(i - 1) if s[i] != "0" else 0
        #     two_digit = ways(i - 2) if i >= 1 and 10 <= int(s[i - 1 : i + 1]) <= 26 else 0
        #     memo[i] = one_digit + two_digit
        #     return memo[i]

        # return ways(len(s) - 1)
