class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)

        # return sorted(s) == sorted(t)

        # This is an O(n) complexity solution

        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in range(len(s)):
            count_s[s[char]] = 1 + count_s.get(s[char], 0)
            count_t[t[char]] = 1+ count_t.get(t[char], 0) 

        for count in count_t:
            # print(count)
            if count_t[count] != count_s.get(count, 0):
                return False

        return True
        
        