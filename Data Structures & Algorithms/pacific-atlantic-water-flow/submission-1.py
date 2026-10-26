class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        atlantic, pacific = set(), set()

        def dfs(r, c, visited, prev_height):
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or (r, c) in visited
                or heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r, c, pacific, heights[r][c])
                if r == ROWS - 1 or c == COLS - 1:
                    dfs(r, c, atlantic, heights[r][c])

        return list(atlantic & pacific)
