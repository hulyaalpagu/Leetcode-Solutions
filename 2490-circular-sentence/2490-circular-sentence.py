class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        words = sentence.split()
        n = len(words)

        for i in range(n):
            if words[i][-1] != words[(i + 1) % n][0]:
                return False
        return True
