class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 3 (hash - array)
        if len(s) != len(t):
            return False
        counts = [0] * 26
        ord_a = ord("a")

        for ch in s:
            counts[ord(ch) - ord_a] += 1
        for ch in t:
            counts[ord(ch) - ord_a] -= 1

        return all(c == 0 for c in counts)

        # ---

        # # solution 2 (hash compare)
        # if len(s) != len(t):
        #     return False

        # count_s, count_t = {}, {}

        # for ch in s:
        #     count_s[ch] = count_s.get(ch, 0) + 1
        # for ch in t:
        #     count_t[ch] = count_t.get(ch, 0) + 1

        # return count_s == count_t

        # ---

        # # solution 1 (sort)
        # if len(s) != len (t):
        #     return False
        # return sorted(s) == sorted(t)
