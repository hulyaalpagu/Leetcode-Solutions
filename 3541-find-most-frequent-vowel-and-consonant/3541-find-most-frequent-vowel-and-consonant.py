class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels=set("aeiou")
        freq={}

        for ch in s:
            freq[ch]=freq.get(ch,0)+1

        max_vowel=0
        max_consonat=0

        for ch,count in freq.items():
            if ch in vowels:
                max_vowel=max(max_vowel,count)
            else:
                max_consonat=max(max_consonat,count)

        return max_vowel + max_consonat
