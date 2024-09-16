class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_seen = {}

        for i in range(len(nums)):
            # print(i)
            difference = target - nums[i]
            if difference in num_seen:
                return [num_seen[difference], i]
            num_seen[nums[i]] = i
        return []