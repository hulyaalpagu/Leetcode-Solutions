class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for num in nums:
            for i in str(num):
                result.append(int(i))
        return  result     

    
