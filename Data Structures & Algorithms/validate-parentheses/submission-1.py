class Solution:
    def isValid(self, s: str) -> bool:
        pattern_dict = {")": "(", "]": "[", "}": "{"}
        openers = ["(","[","{"]
        stack = []
        for st in s:
            if st in openers:
                stack.append(st)
            elif st in pattern_dict:
                if stack and stack[-1] == pattern_dict[st]:
                    stack.pop()
                else:
                    return False
        return not stack
            