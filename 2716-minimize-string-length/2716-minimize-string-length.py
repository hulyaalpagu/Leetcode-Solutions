class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=set()
        count=0
        for i in range(len(s)):
            if s[i] not in result:
                result.add(s[i])
                count+=1
        return count

