class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            board[r][c] = "#"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if backtrack(nr, nc, i + 1):
                    return True
            board[r][c] = word[i]
            return False

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
