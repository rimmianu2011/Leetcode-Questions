class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = 1
        while j in range(len(nums)):
            if nums[i] == nums[j]:
                j = j + 1
            else:
                nums[i+1] = nums[j]
                i = i + 1
                j = j + 1

        return i + 1