class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
        result = []
        stack = []

        def createBrackets(close_b, open_b):

            if open_b == close_b == n:
                result.append("".join(stack))
                return

            if open_b < n:
                stack.append('(')
                createBrackets(close_b, open_b + 1)
                stack.pop()

            if open_b > close_b:
                stack.append(')')
                createBrackets(close_b + 1, open_b)
                stack.pop()


        createBrackets(0, 0)
        # print(result)
        return result