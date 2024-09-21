class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        pre = 1
        post = 1
        i = 1
        result.append(pre)
        while i < len(nums):
            pre *= nums[i-1]
            result.append(pre) 
            i += 1
        print(result)

        i = len(result)
        result[i-1] *= post
        j = i -2
        while j >= 0 :
            post *= nums[j+1]
            result[j] *= post
            j -= 1
        print(result)

        return result
        