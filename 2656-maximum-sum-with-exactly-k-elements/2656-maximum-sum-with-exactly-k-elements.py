class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_result=0
        while k>0:
            max_result=max(nums)
            sum_result+=max_result
            nums.remove(max_result)
            nums.append(max_result+1)
            k-=1
        return sum_result

