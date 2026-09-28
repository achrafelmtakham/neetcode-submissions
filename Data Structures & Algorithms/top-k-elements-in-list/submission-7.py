class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        i = 0
        result = []
        while i < k:
            result.append(max(frequency_dict, key=frequency_dict.get))
            del frequency_dict[max(frequency_dict, key=frequency_dict.get)]
            k -=1
        return result