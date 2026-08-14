class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """
        ["Hello","World"]
        5#hello5#world
        """
        res = []
        i = 0
        while i < len(s):
            delimiter = s.index("#",i)
            start = delimiter + 1
            step = int(s[i:delimiter])
            end = start + step
            res.append(s[start:end])
            i = end
        return res
