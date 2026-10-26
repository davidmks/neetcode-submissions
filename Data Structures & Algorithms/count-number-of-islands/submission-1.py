class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        islands = 0

        def sink(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1":
                return
            grid[r][c] = 0
            for dr, dc in DIRECTIONS:
                sink(dr + r, dc + c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    sink(r, c)
        return islands
