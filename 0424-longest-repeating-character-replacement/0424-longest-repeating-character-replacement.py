class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        l = 0
        max_len = 0

        for r in range(len(s)):
            count_map[s[r]] = 1 + count_map.get(s[r], 0)

            if (r-l+1) - max(count_map.values()) > k:
                count_map[s[l]] = count_map.get(s[l]) - 1
                l += 1

            max_len = max(max_len, r-l+1)
            # print(max_len)
        return max_len

        