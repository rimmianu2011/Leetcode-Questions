class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        j = 0
        i = 0

        while i in range(len(nums)):
            print(i)
            if nums[i] == val:
                nums.pop(i)
                
            else:
                j = j + 1
                i = i + 1
        return j + 1
        