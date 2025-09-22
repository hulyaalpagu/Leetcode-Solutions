class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        d=word.find(ch)
        if d==-1:
            return word

        word_reverse=word[:d+1][::-1]
        word_reverse=word_reverse+word[d+1:]
        return word_reverse
