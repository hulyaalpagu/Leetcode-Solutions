class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels=set("aeiou")
        count=0
        for i in range(len(word)):
            for j in range(i+1,len(word)+1):
                sub=word[i:j]
                if set(sub).issubset(vowels) and vowels.issubset(set(sub)):
                    count+=1
        return count
