class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        track_T, win_size = {}, {}

        for c in t:
            track_T[c] = track_T.get(c, 0) + 1
        
        have, need = 0, len(track_T)
        result, res_len = [-1,-1], float('infinity')
        l = 0
        
        for i in range(len(s)):
            c = s[i]
            win_size[c] = win_size.get(c, 0) + 1

            if c in track_T and win_size[c] == track_T[c]:
                have += 1

            while have == need:
                if (i-l+1) < res_len:
                    result = [l, i]
                    res_len = i-l+1
                win_size[s[l]] -= 1
                if s[l] in track_T and track_T[s[l]] > win_size[s[l]]:
                    have -= 1
                l += 1

        l, r = result

        return s[l:r+1]


        