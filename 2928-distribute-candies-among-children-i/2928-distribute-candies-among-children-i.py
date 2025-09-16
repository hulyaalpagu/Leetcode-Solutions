class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        count=0
        for i in range(limit+1):
            for j in range(limit+1):
                for z in range(limit+1):
                    total=i+j+z
                    if total==n:
                        count+=1
        return count