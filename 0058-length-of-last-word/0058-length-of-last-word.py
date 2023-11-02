class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_words = s.split()

        length = len(list_words)

        lastWord = list_words[length-1]

        outputLength = len(lastWord)

        return outputLength