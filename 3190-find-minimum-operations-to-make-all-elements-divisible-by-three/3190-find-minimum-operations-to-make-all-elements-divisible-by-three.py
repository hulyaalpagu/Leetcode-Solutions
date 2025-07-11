class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            remainder = num % 3
            if remainder != 0:
                # Add the minimal operations needed (1 operation for remainder 1 or 2)
                count += min(remainder, 3 - remainder)
        return count


