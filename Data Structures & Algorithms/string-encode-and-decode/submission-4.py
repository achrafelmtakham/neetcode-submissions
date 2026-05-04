class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # find the next '#' delimiter
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # the string starts right after '#' and is `length` chars long
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result