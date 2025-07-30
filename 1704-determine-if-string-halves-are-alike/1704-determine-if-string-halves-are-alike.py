class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels="aeiouAEIOU"
        half=len(s)//2
        
        count_a=0
        for i in range(half):
           if s[i] in vowels:
            count_a+=1

        count_b=0
        for i in range(half,len(s)):
            if s[i] in vowels:
                count_b+=1

        if count_a==count_b:
            return True
        return False

