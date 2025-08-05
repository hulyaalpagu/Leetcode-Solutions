class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        result1 = []
        result2 = []

        for n1 in set(nums1):
            if n1 not in nums2:
                result1.append(n1)

        for n2 in set(nums2):
            if n2 not in nums1:
                result2.append(n2)

        return [result1, result2]
