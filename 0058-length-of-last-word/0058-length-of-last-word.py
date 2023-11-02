class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_words = s.split()

        length = len(list_words)

        lastWord = list_words[length-1]

        output = len(lastWord)

        return output