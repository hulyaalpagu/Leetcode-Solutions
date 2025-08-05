class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        seen=[]
        for count in freq.values():
            if count in seen:
                return False
            seen.append(count)
        return True
        


      