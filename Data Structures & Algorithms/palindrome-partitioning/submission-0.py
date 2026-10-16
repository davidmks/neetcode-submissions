class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path.copy())
                
            for i in range(start, len(s)):
                if self._is_palindrome(s, start, i):
                    path.append(s[start : i + 1])
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return res

    def _is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
