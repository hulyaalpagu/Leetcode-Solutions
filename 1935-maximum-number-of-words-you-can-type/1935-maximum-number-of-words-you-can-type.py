class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        cnt=0
        words=text.split()
        for word in words:
            can_type=True
            for char in word:
                if char in brokenLetters:
                    can_type =False
                    break
            if can_type==True:
                cnt+=1
        return cnt