class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_number=0
        while n>1:
            if n%2==0:
                total_number+=n//2
                n = n // 2
            else:
                total_number+=(n-1)//2
                n=(n-1)//2+1
        return total_number
