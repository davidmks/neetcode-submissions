class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                on_edge = c in (0, COLS - 1) or r in (0, ROWS - 1)
                if on_edge and board[r][c] == "O":
                    board[r][c] = "T"
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                    board[nr][nc] = "T"
                    q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
