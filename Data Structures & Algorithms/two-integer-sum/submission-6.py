class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, value in enumerate(nums):
            complement = target - value
            if complement in nums_dict:
                return [nums_dict[complement], idx]
            nums_dict[value] = idx