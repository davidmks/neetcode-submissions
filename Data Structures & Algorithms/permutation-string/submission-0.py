class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. solution (array)
        n, m = len(s1), len(s2)
        if n > m:
            return False

        alphabet_lenght = 26
        ord_a = ord("a")
        need = [0] * alphabet_lenght
        window = [0] * alphabet_lenght

        for i in range(n):
            need[ord(s1[i]) - ord_a] += 1
            window[ord(s2[i]) - ord_a] += 1

        matches = sum(need[i] == window[i] for i in range(alphabet_lenght))
        if matches == alphabet_lenght:
            return True

        for right in range(n, m):
            add = ord(s2[right]) - ord_a
            drop = ord(s2[right - n]) - ord_a

            window[add] += 1
            if window[add] == need[add]:
                matches += 1
            elif window[add] == need[add] + 1:
                matches -= 1

            window[drop] -= 1
            if window[drop] == need[drop]:
                matches += 1
            elif window[drop] == need[drop] - 1:
                matches -= 1

            if matches == alphabet_lenght:
                return True

        return False

        # # 2. solution (dict)
        # n, m = len(s1), len(s2)
        # if n > m:
        #     return False

        # need, window = defaultdict(int), defaultdict(int)
        # for i in range(n):
        #     need[s1[i]] +=1
        #     window[s2[i]] +=1

        # have = sum(window[char] == count for char, count in need.items())
        # if have == len(need):
        #     return True

        # for right in range(n, m):
        #     add = s2[right]
        #     drop = s2[right - n]

        #     window[add] += 1
        #     if add in need:
        #         if window[add] == need[add]:
        #             have += 1
        #         elif window[add] == need[add] + 1:
        #             have -= 1

        #     window[drop] -= 1
        #     if drop in need:
        #         if window[drop] == need[drop]:
        #             have += 1
        #         if window[drop] == need[drop] - 1:
        #             have -= 1

        #     if have == len(need):
        #         return True

        # return False
