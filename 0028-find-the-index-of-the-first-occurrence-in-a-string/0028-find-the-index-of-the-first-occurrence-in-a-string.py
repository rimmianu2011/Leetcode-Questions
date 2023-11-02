class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle not in haystack:
            
            print(needle)
            return -1
        else:
            return haystack.index(needle)
