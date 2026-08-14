class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            count[ch] = count.get(ch, 0) - 1

        return all(c == 0 for c in count.values())
