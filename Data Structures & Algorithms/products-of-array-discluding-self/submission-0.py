class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        
        while i <  len(nums):
            facto = 1
            j = 0
            while j <  len(nums):
                if j != i:
                    facto = facto * nums[j]
                j += 1
            i += 1
            result.append(facto)
        return result