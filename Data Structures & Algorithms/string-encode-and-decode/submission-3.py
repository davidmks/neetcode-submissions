class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """5#Hello5#World"""
        i = 0
        result = []
        while i < len(s):
            delimiter = s.index("#", i)
            step = int(s[i:delimiter])
            start = delimiter + 1
            end = start + step
            word = s[start:end]
            result.append(word)
            i = end
        return result
