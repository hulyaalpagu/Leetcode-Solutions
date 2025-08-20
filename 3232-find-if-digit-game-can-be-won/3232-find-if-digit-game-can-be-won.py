class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        single_sum=0
        double_sum=0
        for num in nums:
            if num<10:
                single_sum+=num
            else:
                double_sum+=num
        return single_sum>double_sum or double_sum>single_sum
