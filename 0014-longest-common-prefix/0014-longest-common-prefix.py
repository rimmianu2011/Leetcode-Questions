class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort()

        first_word = strs[0]
        last_word = strs[-1]

        common_letters = []

        if len(strs) == 0:
            return ""

        for i in range(len(strs[0])):            
            if first_word[i] == last_word[i]:
                common_letters.append(first_word[i])
            else:
                break

        common_letters = "".join(common_letters)
        return common_letters