class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        result=[]
        for i in range(0,len(s),k):
            group = s[i:i+k]  # take k characters
            result.append(group)

        if len(result[-1])<k:
            result[-1]=result[-1]+fill*(k-len(result[-1]))
        
        return result

