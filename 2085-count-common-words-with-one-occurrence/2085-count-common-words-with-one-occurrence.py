class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        freq_words1=Counter(words1)
        freq_words2=Counter(words2)
        count=0

        for word,freq in freq_words1.items():
            if freq==1 and freq_words2.get(word,0)==1:
                count+=1
        return count
            