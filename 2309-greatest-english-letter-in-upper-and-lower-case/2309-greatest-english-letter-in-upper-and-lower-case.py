class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters=set(s)
        for c in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if c in letters and c.lower() in letters:
                return c
        return ""