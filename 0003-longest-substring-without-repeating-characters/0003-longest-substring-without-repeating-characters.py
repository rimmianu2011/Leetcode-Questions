class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_s = list(s)
        s_set = set()
        # print(l_s)

        left= 0
        max_length = 0
        

        for right in range(len(l_s)):
            while l_s[right] in s_set:
                s_set.remove(l_s[left])
                left += 1
            s_set.add(l_s[right])

            max_length = max(max_length, right-left+1)

        # print(max_length)
        return max_length