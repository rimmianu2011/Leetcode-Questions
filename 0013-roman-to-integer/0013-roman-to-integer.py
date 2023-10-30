class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        numbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        s_split = list(s)
        total_val = 0

        for i in range(len(s)-1):
            first_val = numbers[s[i]]
            second_val = numbers[s[i+1]]

            if i < len(s) - 1 and first_val < second_val:
                total_val = total_val - first_val 
                
            else:
                total_val = total_val + first_val

            
                

        return total_val + numbers[s[-1]]
        