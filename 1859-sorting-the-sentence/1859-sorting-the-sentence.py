class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split() 
        result=[""]*len(words)
        for word in words:
            num=int(word[-1])
            result[num-1]=word[:-1]   
        return " ".join(result)
            
