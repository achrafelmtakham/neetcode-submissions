class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in  num_set:
                length = 1
                current_position = num
                while current_position + 1 in num_set:
                    length += 1
                    current_position +=1
                longest = max(longest, length)
        return longest