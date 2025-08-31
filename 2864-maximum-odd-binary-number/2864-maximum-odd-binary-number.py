class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        return (c['1']-1)*'1'+c['0']*'0'+'1'


