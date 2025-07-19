class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        nums=sum(grid,[]) #nums = [1, 2, 2, 4]
        n=len(nums) #4
        full=set(range(1,n+1)) # {1, 2, 3, 4}
        seen=set()
        for num in nums:
            if num in seen:
                repeated=num
            else:
                seen.add(num)
        missing=list(full-seen)[0]
        return [repeated,missing]
    


