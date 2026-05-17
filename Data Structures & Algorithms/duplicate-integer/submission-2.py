class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_dict = {}
        for index, num in enumerate(nums):
            if num in seen_dict:
                return True
            else:
                seen_dict[num] = index
        return False