class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        for j in range(n):  # candidate team j
            for i in range(n):  # check every team i
                if grid[i][j] == 1:  # someone beats team j
                    break
            else:
                return j  # no one beats team j

