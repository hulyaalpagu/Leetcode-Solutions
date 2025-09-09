class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        count=Counter(s)
        if letter in count:
            return (count[letter] * 100) // len(s)
        else:
            return 0


