class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left_pointer, right_pointer = i+1, n-1
            while left_pointer < right_pointer:
                total = nums[i] + nums[left_pointer] + nums[right_pointer]
                if total > 0:
                    right_pointer -=1
                elif total < 0:
                    left_pointer +=1
                elif total == 0:
                    result.append([ nums[i] , nums[left_pointer] , nums[right_pointer]])
                    left_pointer +=1
                    while nums[left_pointer] == nums[left_pointer-1] and left_pointer < right_pointer:
                        left_pointer +=1
        return result

        