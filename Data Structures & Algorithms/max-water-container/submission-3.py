class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        left_pointer, right_pointer = 0, n-1
        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            max_area = max(max_area, min(heights[left_pointer], heights[right_pointer]) * width)
            left_height = heights[left_pointer]
            right_height = heights[right_pointer]
            if left_height < right_height:
                left_pointer +=1
            else:
                right_pointer -=1
        return max_area
        