class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_good=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                if num[i:i+3]>max_good:
                    max_good=num[i:i+3]
        return max_good
