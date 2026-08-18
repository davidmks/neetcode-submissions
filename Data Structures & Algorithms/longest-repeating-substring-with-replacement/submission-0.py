class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1. solution (sliding window - optimal)
        left = 0
        best = 0
        freq = {} # O(m) space 26m which can be 1
        max_freq = 0
        for right, char in enumerate(s): # O(n) time
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])

            # Keep the most common letter, replace the rest.
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)
        return best

        # # 2. solution sliding window
        # best = 0
        # for target in set(s):
        #     matching = 0
        #     left = 0
        #     for right, char in enumerate(s):
        #         if char == target:
        #             matching += 1

        #         # Every non-matching letter costs one replacement.
        #         while (right - left + 1) - matching > k:
        #             if s[left] == target:
        #                 matching -= 1
        #             left += 1

        #         best = max(best, right - left + 1)
        # return best
