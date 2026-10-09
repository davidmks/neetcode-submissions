class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        counts = [-c for c in counts.values()]
        heapq.heapify(counts)

        q = deque()
        time = 0

        while counts or q:
            time += 1
            if counts:
                count = 1 + heapq.heappop(counts)
                if count:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                count, time = q.popleft()
                heapq.heappush(counts, count)
        return time
