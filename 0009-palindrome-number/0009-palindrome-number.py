class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        number = x
        if x<0 or x%10 == 0 and x != 0:
            return False
        reverse = 0
        while(number>0):
            reverse = reverse * 10 + number % 10
            number = number // 10
        print(reverse)
        if x == reverse:
            return True
        else:
            return False