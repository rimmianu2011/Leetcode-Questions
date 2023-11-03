class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 2:
            return x

        check = 2

        while check * check <= x:
            check = check + 1

        return check - 1
        