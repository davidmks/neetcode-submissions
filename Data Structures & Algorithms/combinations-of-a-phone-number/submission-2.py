class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        combo = []

        def backtrack(start):
            if start == len(digits):
                res.append("".join(combo.copy()))
                return
            for letter in letters[digits[start]]:
                combo.append(letter)
                backtrack(start + 1)
                combo.pop()

        backtrack(0)
        return res
