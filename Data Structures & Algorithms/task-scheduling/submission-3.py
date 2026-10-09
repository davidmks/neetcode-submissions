class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        h = [-c for c in counts.values()]
        heapq.heapify(h)

        q = deque()  # (remaining, ready_at)
        time = 0

        while h or q:
            time += 1
            if h:
                remaining = -heapq.heappop(h) - 1
                if remaining:
                    ready_at = time + n
                    q.append((remaining, ready_at))
            else:
                time = q[0][1]
            if q and q[0][1] == time:
                remaining, _ = q.popleft()
                heapq.heappush(h, -remaining)
        return time
