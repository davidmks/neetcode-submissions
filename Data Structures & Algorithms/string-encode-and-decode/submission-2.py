class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            delimiter = s.index("#", i)
            step = int(s[i:delimiter])
            start = delimiter + 1
            end = start + step
            output.append(s[start:end])
            i = end
        return output
