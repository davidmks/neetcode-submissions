class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        path = []

        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())
            path.append(airport)

        dfs("JFK")
        return list(reversed(path))
