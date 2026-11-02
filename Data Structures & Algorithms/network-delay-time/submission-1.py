class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        h = [(0, k)]
        visited = set()
        result = 0
        while h:
            time, node = heapq.heappop(h)
            if node in visited:
                continue
            visited.add(node)
            result = time
            for nei, weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(h, (time + weight, nei))
        return result if len(visited) == n else -1
