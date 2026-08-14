class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solution 2 (hash - order)
        groups = defaultdict(list)
        alphabet_lenght = 26
        ord_a = ord("a")

        for word in strs:
            counts = [0] * alphabet_lenght
            for c in word:
                counts[ord(c) - ord_a] += 1
            groups[tuple(counts)].append(word)

        return list(groups.values())
        
        # ---
        
        # # 1. solution (sorting)
        # groups = defaultdict(list)

        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     groups[sorted_word].append(word)

        # return list(groups.values())
