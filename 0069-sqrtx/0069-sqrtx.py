class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 2:
            return x

        # check = 2

        # while check * check <= x:
        #     check = check + 1

        # return check - 1


        start = 0
        end = x

        while abs(start-end) != 1:

            middle = (start + end) // 2

            if middle * middle == x:
                return middle
            if middle * middle > x:
                end = middle
            else:
                start = middle

        return start



        