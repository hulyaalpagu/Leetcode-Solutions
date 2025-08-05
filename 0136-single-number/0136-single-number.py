class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts={}
        for num in nums:
            if num in counts:
                counts[num]+=1
            else:
                counts[num]=1
        for num in counts:
            if counts[num]==1:
                return num