class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for i in range(len(nums)):
            max_num=0
            for j in str(nums[i]):
                max_num=max(int(j),max_num)
            total+=int(str(max_num)*len(str(nums[i])))
        return total

