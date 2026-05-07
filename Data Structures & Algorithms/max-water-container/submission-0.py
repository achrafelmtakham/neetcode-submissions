class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        surface_list = []
        for i in range(n):
            for j in range(n-1,-1,-1):
                surface_list.append((j-i)*min(heights[j],heights[i]))
        return max(surface_list)
        