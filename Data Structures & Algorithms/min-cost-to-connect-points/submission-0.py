class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0, 0)]
        total = 0

        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            total += cost
            xi, yi = points[i]
            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    man_dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(heap, (man_dist, j))
        return total
