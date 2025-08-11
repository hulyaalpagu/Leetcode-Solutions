class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        result=0
        for w in words:
            for letter in w:
                if w.count(letter)>chars.count(letter):
                    break
            else:
                result+=len(w)
        return result