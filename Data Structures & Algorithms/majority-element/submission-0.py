class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seuil = len(nums) // 2
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        for item in frequency_dict:
            if frequency_dict[item] > seuil:
                return item