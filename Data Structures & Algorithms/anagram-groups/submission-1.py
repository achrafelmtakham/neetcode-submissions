class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in result_dict:
                result_dict[sorted_str] = []
            result_dict[sorted_str].append(s)
        return list(result_dict.values())