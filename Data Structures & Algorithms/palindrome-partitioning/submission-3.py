class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def is_pali(word):
            return word == word[::-1]

        def backtrack(start):
            if start == len(s):
                res.append(part.copy())
                return
            for end in range(start, len(s)):
                word = s[start:end+1]
                if not is_pali(word):
                    continue
                part.append(word)
                backtrack(end + 1)
                part.pop()

        backtrack(0)
        return res
