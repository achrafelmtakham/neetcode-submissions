class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char) - ord('a')] +=1
            result_dict[tuple(count)].append(s)
        return list(result_dict.values())