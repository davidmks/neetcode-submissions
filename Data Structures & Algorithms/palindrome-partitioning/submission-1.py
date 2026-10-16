class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substring = []

        def is_pali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start):
            if start == len(s):
                res.append(substring.copy())
                return

            for i in range(start, len(s)):
                if is_pali(start, i):
                    substring.append(s[start : i + 1])
                    backtrack(i + 1)
                    substring.pop()

        backtrack(0)
        return res
