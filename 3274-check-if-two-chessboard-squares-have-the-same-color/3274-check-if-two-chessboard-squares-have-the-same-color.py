class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        col1=ord(coordinate1[0])-ord('a')+1
        col2=ord(coordinate2[0])-ord('a')+1

        row1=int(coordinate1[1])
        row2=int(coordinate2[1])

        if (col1%2==row1%2 and col2%2==row2%2) or \
           (col1%2!=row1%2 and col2%2!=row2%2):
           return True
        else:
            return False
    

