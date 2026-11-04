class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 0

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > max_len:
                start, max_len = left + 1, right - left - 1

        for i in range(len(s)):
            expand(i, i)  # odd
            expand(i, i + 1)  # even

        return s[start : start + max_len]
