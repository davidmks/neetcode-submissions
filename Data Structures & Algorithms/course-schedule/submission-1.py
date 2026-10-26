class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        q = deque(c for c in range(numCourses) if indegree[c] == 0)

        taken = 0
        while q:
            node = q.popleft()
            taken += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return True if taken == numCourses else False
