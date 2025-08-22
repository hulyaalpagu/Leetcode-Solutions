class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digit=sorted(str(num))
        num1,num2="",""
        i=0

        for dgt in digit:
            if i%2==0:
                num1+=dgt
            else:
                num2+=dgt
            i+=1
        return int(num1)+int(num2)
