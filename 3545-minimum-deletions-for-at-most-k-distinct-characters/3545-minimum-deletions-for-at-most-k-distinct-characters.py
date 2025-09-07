class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s_count=Counter(s) # Counter({'y':3, 'z':2})
        counts=sorted(s_count.values())  # [2, 3]
        removed=0
        to_remove=len(counts)-k  # 2 - 1 = 1

        for i in range(to_remove):
            removed+=counts[i]
        
        return removed
 