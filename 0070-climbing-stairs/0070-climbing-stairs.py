class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        steps = []
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            steps.append(1)
            steps.append(2)

        for i in range(3, n+1):
            steps.append(steps[i-2] + steps[i-3])

        return steps[len(steps) - 1]