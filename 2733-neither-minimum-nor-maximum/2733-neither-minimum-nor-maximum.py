class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return -1

        max_nums=max(nums)
        min_nums=min(nums)

        for num in nums:
            if num!=max_nums and num!=min_nums:
                return num
        return -1