class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            "}":"{", "]":"[", ")":"("
        }

        for char in s: 
            #closed 
            if char in close_to_open:
                if stack and close_to_open[char] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(char)
            
        if stack: 
            return False
        else: 
            return True

            #open 
            
            #first one cannot be closed
            #it has to be correct closed one

            #in stack we will put opens and if we see a closed we pop from
            #the stack