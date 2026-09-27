class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_dict = {}
        result = ""
        for char in s:
            char_dict[char] = char_dict.get(char, 0) +1
        for char in order:
            if char in char_dict:
                result += "".join([char]*char_dict[char])
                del char_dict[char]
        result += "".join(char * count for char, count in char_dict.items())
        return result