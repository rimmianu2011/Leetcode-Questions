class Solution:
    def isHappy(self, n: int) -> bool:
        visited  = set()

        while n not in visited:
            visited.add(n)

            if n == 1:
                return True

            n = self.sumOfDigit(n)

        return False

    def sumOfDigit(self, n: int) -> int:
        sum_n = 0
        while n:
            digit = n % 10
            # print(digit)
            sum_n += digit**2
            n = n // 10
        # print(sum_n)
        return sum_n
        