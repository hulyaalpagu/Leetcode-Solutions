class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        tested=0
        for battery in batteryPercentages:
            if battery>tested:
                tested+=1
        return tested