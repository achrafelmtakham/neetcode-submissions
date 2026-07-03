class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else: 
            t_dict = {}
            s_dict = {}
            n = len(s)
            for i in range(n):
                if t[i] in t_dict:
                    t_dict[t[i]] +=1
                elif t[i] not in t_dict:
                    t_dict[t[i]] = 1
                if s[i] in s_dict:
                    s_dict[s[i]] +=1
                elif s[i] not in s_dict:
                    s_dict[s[i]] = 1
            return s_dict == t_dict