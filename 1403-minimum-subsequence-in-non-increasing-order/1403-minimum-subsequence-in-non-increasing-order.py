class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        total=sum(nums)
        chosen,curr_sum=[],0

        for num in nums:
            chosen.append(num)
            curr_sum+=num
            if curr_sum>total-curr_sum:
                break
        return chosen
