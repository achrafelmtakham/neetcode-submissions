class Solution:
    def maxDifference(self, s: str) -> int:
        frequency_dict = {}
        max_odd_freq, min_even_freq = 0, 0
        for char in s:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        for item, frequency in frequency_dict.items():
            if (frequency % 2)  != 0:
                max_odd_freq = max(max_odd_freq, frequency)
            else:
                if min_even_freq == 0:
                    min_even_freq = frequency
                else:
                    min_even_freq = min(min_even_freq, frequency)
        return max_odd_freq - min_even_freq