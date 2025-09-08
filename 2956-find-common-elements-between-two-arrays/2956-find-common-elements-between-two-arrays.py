class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count_n1=0
        count_n2=0
        
        for n1 in nums1:
            if n1 in nums2:
                count_n1+=1
        
        for n2 in nums2:
            if n2 in nums1:
                count_n2+=1

        return [count_n1,count_n2]