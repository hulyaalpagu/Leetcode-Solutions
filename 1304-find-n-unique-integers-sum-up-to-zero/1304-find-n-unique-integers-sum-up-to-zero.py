class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result=[]
        total_min=0
        for i in range(1,n):
            result.append(i)

        result.append(-sum(result))
        return result

        



