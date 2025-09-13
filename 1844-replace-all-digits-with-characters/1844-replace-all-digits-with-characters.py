class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)

        for i in range(1,len(s),2):
            prev_char=s[i-1]
            digit=int(s[i])
            s[i]=chr(ord(prev_char)+digit)
            
        return "".join(s)
