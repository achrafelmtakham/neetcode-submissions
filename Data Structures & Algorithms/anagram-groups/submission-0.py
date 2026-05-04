class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        srt_dict = {}
        for srt in strs:
            anagram = "".join(sorted(srt))
            if anagram in srt_dict:
                srt_dict[anagram].append(srt)
            else:
                srt_dict[anagram] = [srt]
        result = [value for value in srt_dict.values()]
        return result