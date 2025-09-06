class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        answer=0
        while grid[0]:
            removed=[]
            for row in grid:
                max_val=max(row)
                row.remove(max_val)
                removed.append(max_val)
            answer+=max(removed)
        return answer
