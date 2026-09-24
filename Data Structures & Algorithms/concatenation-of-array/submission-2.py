class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concatinated_array = [num for num in nums]
        for num in nums:
            concatinated_array.append(num)
        return concatinated_array
        