class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(0,len(nums),2):
            freq=nums[i]
            val=nums[i+1]
            while freq>0:
                result.append(val)
                freq-=1
        return result

        
