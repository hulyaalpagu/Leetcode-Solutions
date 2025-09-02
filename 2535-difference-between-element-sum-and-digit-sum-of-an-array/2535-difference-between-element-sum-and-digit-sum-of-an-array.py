class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digit_num=0
        element_sum=0
        for num in nums:
            element_sum+=num
            while num>0:
                digit_num+=num%10
                num=num//10
        return abs(element_sum-digit_num)
            