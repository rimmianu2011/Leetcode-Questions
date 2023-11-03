class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = list(map(int, a))
        b = list(map(int, b))

        i = len(a) - 1
        j = len(b) - 1

        output = []
        carry = 0

        while i >= 0 or j >= 0 or carry == 1:
            if i>= 0:
                x = a[i]
            else:
                x = 0
            if j>=0:
                y = b[j]
            else:
                y = 0

            sum = x + y + carry
            carry = sum // 2
            output = [sum % 2] + output

            i -= 1
            j -= 1

        return ''.join(map(str, output))