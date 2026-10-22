class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        time, fresh_count = 0, 0
        fresh, rotten = 1, 2
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == fresh:
                    fresh_count += 1
                elif grid[r][c] == rotten:
                    q.append((r, c))

        while q and fresh_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == fresh:
                        grid[nr][nc] = rotten
                        fresh_count -= 1
                        q.append((nr, nc))
            time += 1

        return time if fresh_count == 0 else -1
