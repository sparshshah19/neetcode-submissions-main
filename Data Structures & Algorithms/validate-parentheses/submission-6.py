class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            "}":"{",
            "]":"[", 
            ")":"("
        }

        for char in s:
            if stack and char in close_to_open:
                if stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        else: 
            return True
