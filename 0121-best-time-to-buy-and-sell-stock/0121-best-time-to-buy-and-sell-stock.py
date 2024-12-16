class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_prof = 0

        while right < len(prices):

            if prices[left] < prices[right]:
                max_prof = max(max_prof, (prices[right] - prices[left]))
                right += 1

            else:
                left = right
                right += 1
                # print(right)
                # print(max_prof)
        # print(max_prof)
        return max_prof