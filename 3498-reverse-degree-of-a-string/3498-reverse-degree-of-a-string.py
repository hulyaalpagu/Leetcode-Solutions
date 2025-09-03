class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        for i in range(len(s)):
            rev_index=26-(ord(s[i])-ord('a'))
            total+=rev_index*(i+1)
        return total


