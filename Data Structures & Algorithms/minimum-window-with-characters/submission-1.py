class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for char in t:
            need[char] += 1
        required = len(need)

        window = defaultdict(int)
        left = 0
        matches = 0
        best_len = float("inf")
        best_start = 0

        for right, char in enumerate(s):
            window[char] += 1
            if char in need:
                if need[char] == window[char]:
                    matches += 1

            while matches == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                drop = s[left]
                window[drop] -= 1
                if drop in need:
                    if window[drop] == need[drop] - 1:
                        matches -= 1
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_start : best_start + best_len]
