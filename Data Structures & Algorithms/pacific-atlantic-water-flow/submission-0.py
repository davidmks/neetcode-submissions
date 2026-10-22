class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        atlantic, pacific = set(), set()

        def dfs(r, c, prev_height, visited):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in visited
                or heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], visited)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, cols - 1, heights[r][cols - 1], atlantic)

        for c in range(cols):
            dfs(0, c, heights[0][c], pacific)
            dfs(rows - 1, c, heights[rows - 1][c], atlantic)

        return list(pacific & atlantic)
