class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(x):
            s=0
            while x>0:
                s+=x%10
                x//=10
            return s
        for i in range(len(nums)):
            if digit_sum(nums[i])==i:
                return i
        return -1

