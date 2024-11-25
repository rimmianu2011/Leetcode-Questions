import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.checkS(s[l]):
                l += 1
            while r > l and not self.checkS(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True
        
    def checkS(self, n):
        return (ord('A') <= ord(n) <= ord('Z') or
               ord('a') <= ord(n) <= ord('z') or
               ord('0') <= ord(n) <= ord('9'))


        # solution 1
        # s_new = re.sub(r'[^a-zA-Z0-9\s]', '', s)
        # s_new = s_new.lower()
        # s_new = "".join(s_new.split())
        # s = list(s_new)
        # s_flipped = []
        # for i in s[::-1]:
        #     s_flipped.append(i)
        # s_f = ''.join(s_flipped)

        # if s_f == s_new:
        #     return True
        # else:
        #     return False

        