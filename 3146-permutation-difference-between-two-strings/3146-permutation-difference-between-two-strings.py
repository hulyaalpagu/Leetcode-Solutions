class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        total=0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    total+=abs(i-j)
        return total