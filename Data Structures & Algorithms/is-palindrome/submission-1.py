import string

IGNORE = string.punctuation + string.whitespace


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join([ word.strip(IGNORE).lower() for word in s if len(word.strip(IGNORE)) > 0 ])

        right_pointer , left_pointer = 0 , len(cleaned_s) -1

        while right_pointer < left_pointer:
            if cleaned_s[right_pointer] != cleaned_s[left_pointer]:
                return False
            right_pointer += 1
            left_pointer -= 1

        return True