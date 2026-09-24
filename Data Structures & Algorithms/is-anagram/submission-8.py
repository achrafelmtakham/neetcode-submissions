class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0)+ 1
        return t_dict == s_dict