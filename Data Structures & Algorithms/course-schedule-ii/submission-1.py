class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        q = deque(c for c in range(numCourses) if indegree[c] == 0)

        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return order if len(order) == numCourses else []
