class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        biggest=max(nums)
        nums.remove(biggest)

        second_biggest =max(nums)
        nums.remove(second_biggest)

        smallest=min(nums)
        nums.remove(smallest)

        second_smallest=min(nums)

        return (biggest*second_biggest)-(smallest*second_smallest)
        