class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        for num in nums:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd

            