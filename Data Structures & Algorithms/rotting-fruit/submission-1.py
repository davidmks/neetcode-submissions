class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        EMPTY, FRESH, ROTTEN = 0, 1, 2

        fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == FRESH:
                    fresh += 1
                elif grid[r][c] == ROTTEN:
                    q.append((r, c))
        minute = 0
        while q and fresh:
            minute += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN
                        fresh -= 1
                        q.append((nr, nc))
        
        return minute if fresh == 0 else -1
