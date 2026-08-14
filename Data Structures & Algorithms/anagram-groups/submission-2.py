class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        aphabet_lenght = 26
        ord_a = ord('a')

        for s in strs:
            freq = [0] * aphabet_lenght
            for char in s:
                freq[ord(char)-ord_a] += 1
            groups[tuple(freq)].append(s)
        return list(groups.values())

        