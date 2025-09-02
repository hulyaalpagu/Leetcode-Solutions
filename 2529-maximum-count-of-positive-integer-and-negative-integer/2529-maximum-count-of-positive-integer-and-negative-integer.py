class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive_cnt=0
        negative_cnt=0
        for num in nums:
            if num>0:
                positive_cnt+=1
            elif num<0:
                negative_cnt+=1
        return max(positive_cnt,negative_cnt)