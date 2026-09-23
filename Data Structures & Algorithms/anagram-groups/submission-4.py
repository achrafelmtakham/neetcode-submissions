class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for srt in strs:
            count = [0]*26
            for char in srt:
                count[ord(char) - ord('a')] +=1
            result[tuple(count)].append(srt)
        return list(result.values())