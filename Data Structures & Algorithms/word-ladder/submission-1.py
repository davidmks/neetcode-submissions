class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def patterns(word):
            return [word[:i] + "*" + word[i + 1 :] for i in range(len(word))]

        buckets = defaultdict(list)
        for word in wordList:
            for p in patterns(word):
                buckets[p].append(word)

        q = deque([beginWord])
        seen = {beginWord}
        length = 0
        while q:
            length += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return length
                for p in patterns(word):
                    for nxt in buckets[p]:
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)
        return 0

