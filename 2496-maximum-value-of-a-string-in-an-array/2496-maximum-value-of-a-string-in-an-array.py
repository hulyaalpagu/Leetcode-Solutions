class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max_val=0
        for s in strs:
            if s.isdigit():
                val=int(s)
            else:
                val = len(s)    # contains letters → length
            max_val = max(max_val, val)
        return max_val
    
  