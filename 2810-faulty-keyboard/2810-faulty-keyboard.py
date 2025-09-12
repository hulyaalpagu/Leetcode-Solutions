class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        text=""
        for ch in s:
            if ch=='i':
                text=text[::-1]
            else:
                text+=ch
        return text
            
