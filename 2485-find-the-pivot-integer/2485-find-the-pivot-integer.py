class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        left_total,total=0,0
        for i in range(1,n+1):
            total+=i
        
        for i in range(1,n+1):
            left_total+=i
            if left_total==total-left_total+i:
                return i
        return -1