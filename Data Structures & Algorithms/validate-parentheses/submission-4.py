class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "]": "[", "}": "{"}
        openers = {"(", "[", "{"}
        stack = []
        for char in s:
            if char in openers:
                stack.append(char)
            elif char in close_to_open:
                if not stack or stack.pop() != close_to_open[char]:
                    return False
        return not stack