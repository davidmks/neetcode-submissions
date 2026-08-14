class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1 (sort)
        if len(s) != len (t):
            return False
        return sorted(s) == sorted(t)
        # # solution 2 (hash - array)       
        # if len(s) != len(t):
        #     return False

        # count = [0] * 26
        # ord_a = ord("a")

        # for ch in s:
        #     count[ord(ch) - ord_a] += 1
        # for ch in t:
        #     count[ord(ch) - ord_a] -= 1

        # return all(c == 0 for c in count)
