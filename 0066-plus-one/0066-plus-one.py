class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits) - 1

        while length >= 0:

            if digits[length] == 9:
                digits[length] = 0
                length = length - 1
                
            else:
                digits[length] += 1
                return digits
                
        return [1] + digits
        