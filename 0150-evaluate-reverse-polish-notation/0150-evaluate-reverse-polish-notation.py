class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '/', '*']
        stack = []
        out = 0
        for num in tokens:
            if num in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                out = int(eval(num1 + num + num2))
                stack.append(str(out))
                
            else:
                stack.append(num)

        return int(stack.pop())