class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n-1):
            result.append(max(arr[i+1:n]))
        result.append(-1)
        return result