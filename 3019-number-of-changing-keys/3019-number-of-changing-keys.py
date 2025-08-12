class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=0
        s=s.lower()
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                cnt+=1
        return cnt
