class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        count = [[] for i in range(len(nums) + 1)]
        for num,v in frequency_dict.items():
            count[v].append(num)
        result = [  ]
        for i in range(len(count)-1, 0, -1):
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result