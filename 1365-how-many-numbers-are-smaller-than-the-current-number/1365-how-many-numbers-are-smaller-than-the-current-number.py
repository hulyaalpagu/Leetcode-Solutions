class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            count = 0  # reset count for each i
            for j in range(len(nums)):  # compare with all elements
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result
