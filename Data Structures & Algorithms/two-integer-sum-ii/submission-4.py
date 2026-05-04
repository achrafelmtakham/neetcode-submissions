class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left_pointer , right_pointer = 0 , len(numbers) -1
        while left_pointer < right_pointer :
            sum_pointers = numbers[left_pointer] + numbers[right_pointer]
            if sum_pointers > target:
                right_pointer -= 1
            elif sum_pointers < target:
                left_pointer += 1
            elif sum_pointers == target:
                return [left_pointer + 1 , right_pointer + 1]
        return []
        