class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        lst = {'a': '0','b': '1', 'c': '2','d': '3','e': '4','f': '5','g': '6','h': '7','i': '8','j': '9'}
        first_num=""
        second_num=""
        target_num=""
        for f in firstWord:
            if f in lst:
                first_num+=lst[f]

        for s in secondWord:
            if s in lst:
                second_num+=lst[s]

        for t in targetWord:
            if t in lst:
                target_num+=lst[t]

        total=int(first_num) + int(second_num)
        return total==int(target_num)

            
