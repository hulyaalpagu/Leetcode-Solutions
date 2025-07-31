class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt=0
        for row in grid:
            for num in row:
                if num<0:
                    cnt+=1
        return cnt


    