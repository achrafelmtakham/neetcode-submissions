class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in parentheses_dict.values():
                stack.append(char)
            elif char in parentheses_dict:
                if stack and stack[-1] == parentheses_dict[char]:
                    stack.pop()
                else:
                    return False
        return not stack