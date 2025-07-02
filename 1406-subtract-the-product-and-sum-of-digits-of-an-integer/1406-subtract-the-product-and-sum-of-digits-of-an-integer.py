class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        total = 0
        
        for digit in str(n):
            num = int(digit)
            product *= num
            total += num
        
        return product - total
