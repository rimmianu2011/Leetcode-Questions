class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)
        pre = 1
        post = 1
        i = 1
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i] 
        # print(result)

        i = len(result)
        result[i-1] *= post
        j = i -2
        while j >= 0 :
            post *= nums[j+1]
            result[j] *= post
            j -= 1
        # print(result)

        return result
        