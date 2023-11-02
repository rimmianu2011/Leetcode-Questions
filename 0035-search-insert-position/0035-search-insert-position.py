class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        output = 0

        for i in range(len(nums)):

            if nums[i] == target:
                output = i
                # break
                return output
            elif target not in nums and target > nums[i]:
                output = i + 1
            elif target not in nums and target < nums[i]:
                output = i 
                # break
                return output

        return output


        