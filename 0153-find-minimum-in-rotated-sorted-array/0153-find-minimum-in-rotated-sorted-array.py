class Solution:

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        max_n = 0
        min_n = max(nums)

        if len(nums) == 1:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2
            
            if nums[left] <= nums[mid] and nums[right] <= nums[left]:
                print(mid)
                min_n = min(nums[mid], min_n)
                left = mid + 1
            else:
                right = mid - 1
                min_n = min(nums[mid], min_n)
            print('min: ', min_n)
        print(min_n)
        return min_n


    
        