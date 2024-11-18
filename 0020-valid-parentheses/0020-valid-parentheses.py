class Solution:
    def isValid(self, s: str) -> bool:
        
        stack_s = []
        s = list(s)

        close_open_paran = {")":"(", "}":"{", "]":"["}

        for braq in s:

            if braq in close_open_paran:
                
                if stack_s and stack_s[-1] == close_open_paran[braq]:
                    stack_s.pop()

                else:
                    return False

            else:
                stack_s.append(braq)
        

        return True if not stack_s else False
            