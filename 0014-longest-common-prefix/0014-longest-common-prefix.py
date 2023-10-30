class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort()
        common_letters = []

        if len(strs) == 0:
            return ""

        for i in range(len(strs[0])):            
            if strs[0][i] == strs[-1][i]:
                common_letters.append(strs[0][i])
            else:
                break

        common_letters = "".join(common_letters)
        return common_letters