class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        max_cells =n*n
        max_by_weight =maxWeight//w
        return min(max_cells,max_by_weight)