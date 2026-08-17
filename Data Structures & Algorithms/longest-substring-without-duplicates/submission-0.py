class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. solution (sliding window)
        seen = set()
        left = 0
        longest = 0
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            longest = max(longest, right - left + 1)
        return longest

        # # 2. solution (optimization)
        # seen = {}
        # left = 0
        # longest = 0
        # for right, char in enumerate(s):
        #     while char in seen and seen[char] >= left:
        #         left = seen[char] + 1
        #     seen[char] = right
        #     longest = max(longest, right - left + 1)
        # return longest
