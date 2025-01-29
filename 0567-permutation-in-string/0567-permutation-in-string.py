class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        l = 0
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1 

        total_matches = 0

        for j in range(26):
            if s1Count[j] == s2Count[j]:
                total_matches += 1
        
        for r in range(len(s1), len(s2)):
            if total_matches == 26:
                return True
            i = ord(s2[r]) - ord('a')
            s2Count[i] += 1

            if s1Count[i] == s2Count[i]:
                total_matches += 1
            elif s1Count[i] + 1 == s2Count[i]:
                total_matches -= 1


            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                total_matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                total_matches -= 1
            
            l += 1
        if total_matches == 26:
            return True
        return False