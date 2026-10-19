class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(start):
            if start == len(s):
                res.append(part.copy())
                return
            for end in range(start, len(s)):
                word = s[start : end + 1]
                if not word == word[::-1]:
                    continue
                part.append(word)
                backtrack(end + 1)
                part.pop()
            pass

        backtrack(0)
        return res
