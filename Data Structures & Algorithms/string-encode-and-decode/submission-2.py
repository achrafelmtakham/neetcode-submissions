class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
            
        encoded_str = "".join(parts)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':   # scan right to find the separator
                j += 1
            length = int(s[i:j]) # parse the length prefix
            result.append(s[j+1 : j+1+length])  # slice exactly `length` chars
            i = j + 1 + length   # jump i past this token entirely
        return result
            