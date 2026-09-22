class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        result = 0
        for right, char in enumerate(s):
            counts[char] += 1
            most_freq_char = max(counts, key=counts.get)
            most_freq = counts[most_freq_char]

            while (right - left + 1) - most_freq > k:
                counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        return result
