class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length = 0
        longest_len = 0

        for i in nums:
            if i-1 not in num_set:
                length = 1
                while i+length in num_set:
                    length += 1
                longest_len = max(length, longest_len)
            # print(length)    
        return longest_len