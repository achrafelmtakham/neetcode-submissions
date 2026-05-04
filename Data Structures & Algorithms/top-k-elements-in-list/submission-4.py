class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] +=1
            else:
                nums_dict[num] = 1
        freq_pairs = []
        for num in nums_dict:
            freq_pairs.append((nums_dict[num], num))
        freq_pairs.sort(reverse=True)
        result = []
        for i in range(k):
            result.append(freq_pairs[i][1])
        return result