class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_nums = [1] * n
        rights_nums = [1] * n
        for i in range(1,n):
            left_nums[i] = left_nums[i-1] * nums[i-1]
        
        for i in range(n-2,-1,-1):
            rights_nums[i] = rights_nums[i+1] * nums[i+1]
        result = []
        for i in range(n):
            result.append(rights_nums[i] * left_nums[i])
        return result
        