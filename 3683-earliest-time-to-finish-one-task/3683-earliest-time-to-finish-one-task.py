class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        time_to_finish=float('inf')
        for task in tasks:
            finish=0
            for t in task:
                finish+=t
            time_to_finish=min(finish,time_to_finish)
        return time_to_finish
        