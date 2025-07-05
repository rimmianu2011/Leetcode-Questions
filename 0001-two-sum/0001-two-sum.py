class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     # print(nums[i])
        #     for j in range(1, len(nums)):
        #         # print(nums[j])
        #         if nums[i] + nums[j] == target:
        #             # print(i,j)
        #             return [i,j]
        hash_set = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_set:
                curr = i
                exist = hash_set[diff]
                return [exist, curr]
            # if nums[i] not in hash_set:
            #     hash_set[nums[i]] = i
            else:
                hash_set[nums[i]] = i
            