class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_words = s.split()
        # print(s)

        length = len(list_words)
        # print(length)

        lastWord = list_words[length-1]
        # print(len(lastWord))

        output = len(lastWord)

        return output