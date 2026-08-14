class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for a, b in zip(s, t):
            count_s[a] = count_s.get(a, 0) + 1
            count_t[b] = count_t.get(b, 0) + 1
        
        return count_s == count_t
