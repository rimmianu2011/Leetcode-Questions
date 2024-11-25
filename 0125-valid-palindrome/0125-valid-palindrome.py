import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = re.sub(r'[^a-zA-Z0-9\s]', '', s)
        s_new = s_new.lower()
        s_new = "".join(s_new.split())
        s = list(s_new)
        s_flipped = []
        for i in s[::-1]:
            s_flipped.append(i)
        s_f = ''.join(s_flipped)

        if s_f == s_new:
            return True
        else:
            return False
        print(s_f)
        print(s_new)

        