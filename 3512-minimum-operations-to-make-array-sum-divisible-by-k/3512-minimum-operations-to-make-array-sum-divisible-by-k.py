class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        remainder = sum(nums) % k
        if remainder != 0:
            return remainder
        else:
            return 0
