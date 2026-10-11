class Twitter:
    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((tweetId, self.time))

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        for uid in self.following[userId].union({userId}):
            if self.tweets[uid]:
                last = len(self.tweets[uid]) - 1
                tid, time = self.tweets[uid][last]
                heapq.heappush(h, (-time, tid, uid, last))

        feed = []
        while h and len(feed) < 10:
            _, tid, uid, last = heapq.heappop(h)
            feed.append(tid)
            if last > 0:
                last -= 1
                tid, time = self.tweets[uid][last]
                heapq.heappush(h, (-time, tid, uid, last))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return None
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
