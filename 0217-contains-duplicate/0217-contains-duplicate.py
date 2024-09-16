class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_exists = set()

        for n in nums:
            # print(n)
            if n in num_exists:
                return True
            num_exists.add(n)
        return False