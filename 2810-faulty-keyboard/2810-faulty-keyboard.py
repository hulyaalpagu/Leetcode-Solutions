class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        text=[]
        for ch in s:
            if ch=='i':
                text.reverse()
            else:
                text.append(ch)
        return "".join(text)
            
