class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        first_letters=""
        for word in words:
            first_letters+=word[0]

        return first_letters==s
