class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue 

            l, r = i+1, len(nums) - 1
            while l < r:
                val = n + nums[l] + nums[r]
                # print('n + nums[l] + nums[r]', n, nums[l], nums[r])
                if val > 0:
                    r -= 1
                elif val < 0:
                    l += 1
                else:
                    output.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l+= 1
        return output