class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        merged=[]
        for i in range(m):
            merged.append(nums1[i])
        for j in range(n):
            merged.append(nums2[j])
        merged.sort()

        for z in range(m+n):
            nums1[z]=merged[z]