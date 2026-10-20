class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            "}":"{", "]":"[", ")":"("
        }

        for char in s: 
            #if its closed we are going to check if it matches with the correct one from close_to_open 
            #and then if yes, we will pop the open one from the stack. 
            #if its open, we are going to just append to the stack. 

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


        #the first one has to be open

        #stack ----   [     