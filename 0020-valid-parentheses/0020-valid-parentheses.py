class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        output = False
        stack = []
        for i in range(len(s)):
            if len(s) % 2 != 0:
                output = False
                break

            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])

            if s[i] == ')' or s[i] == ']' or s[i] == '}':
                if not stack:
                    output = False
                    break

                popped_val = stack.pop()

                if (popped_val == '(' and s[i] == ')') or (popped_val == '[' and s[i] == ']') or (popped_val == '{' and s[i] == '}'):
                    output = True
        
                else:
                    output = False
                    break
        if stack:
            output = False
            
        return output