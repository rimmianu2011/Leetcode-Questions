class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        prod = 1
        result = 0

        for r in range(len(nums)):
            prod = prod * nums[r]
            while prod >= k and l<=r:
                prod = prod // nums[l]
                l += 1
             
            result += (r-l+1)
        return result
            