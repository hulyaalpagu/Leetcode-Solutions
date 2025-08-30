class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        sorted_words=[None]*len(words)

        for word in words:
            position=int(word[-1])-1
            sorted_words[position]=word[:-1]
        return " ".join(sorted_words)
