class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        surface_list = []
        left_pointer, right_pointer = 0, n-1
        while left_pointer < right_pointer:
            surface_list.append(min(heights[left_pointer], heights[right_pointer]) * len(heights[left_pointer:right_pointer]))
            left_height = heights[left_pointer]
            right_height = heights[right_pointer]
            if left_height < right_height:
                left_pointer +=1
            else:
                right_pointer -=1
        return max(surface_list)
        