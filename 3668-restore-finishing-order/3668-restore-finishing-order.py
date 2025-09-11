class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        result=[]
        for o in order:
            if o in friends:
                result.append(o)

        return result
