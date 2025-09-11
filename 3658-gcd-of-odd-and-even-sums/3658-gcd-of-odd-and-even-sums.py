class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumOdd=0
        sumEven=0
        for i in range(1,n+1):
            sumOdd+=2*i -1
            sumEven+=2*i

        while sumEven != 0:
            sumOdd, sumEven = sumEven, sumOdd % sumEven
        
        return sumOdd