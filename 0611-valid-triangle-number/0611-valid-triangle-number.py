class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count = 0
        
        for k in range(n - 1, 1, -1): 
            left, right = 0, k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += (right - left)   # all valid pairs
                    right -= 1
                else:
                    left += 1
        return count
