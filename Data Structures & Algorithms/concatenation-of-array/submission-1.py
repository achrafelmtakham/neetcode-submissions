class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concatinated_array = [0]* (2*len(nums))
        for idx, num in enumerate(nums):
            concatinated_array[idx] = concatinated_array[idx + len(nums)] = num
        return concatinated_array
        