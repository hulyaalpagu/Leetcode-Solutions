class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_total=10000
        result=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    total=i+j
                    if total<min_total:
                        min_total=total
                        result=[list1[i]]
                    elif total==min_total:
                        result.append(list1[i])
        return result
