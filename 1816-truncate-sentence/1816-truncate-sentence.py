class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        words=s.split()
        result=""
        for i in range(k):
            result +=words[i]
            if i<k-1:
                result +=" "
        return result
    