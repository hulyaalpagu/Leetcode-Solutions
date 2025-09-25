class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        distinct_nums=sorted(set(nums),reverse=True)
        return distinct_nums[:k]
