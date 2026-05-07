class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window_count = {}
        max_length = 0
        
        for right in range(len(s)):
            new_letter = s[right]
            window_count[s[right]] = window_count.get(s[right], 0) + 1

            while (right - left + 1) - max(window_count.values()) > k:
                window_count[s[left]] -= 1
                left +=1

            max_length = max(max_length, right - left + 1)
        return max_length