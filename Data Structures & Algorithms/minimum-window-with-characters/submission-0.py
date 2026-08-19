class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        want = {}
        for ch in t:
            want[ch] = want.get(ch, 0) + 1

        need, have = len(want), 0
        window = {}
        best_len, best_start, left = float("inf"), 0, 0

        for right, ch in enumerate(s):
            if ch in want:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == want[ch]:
                    have += 1

            while have == need:
                if right - left + 1 < best_len:
                    best_len, best_start = right - left + 1, left

                drop = s[left]
                if drop in want:
                    if window[drop] == want[drop]:
                        have -= 1
                    window[drop] -= 1
                left += 1

        return s[best_start:best_start + best_len] if best_len != float("inf") else ""
