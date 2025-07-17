class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude=0
        max_altitude =0
        for i in range(len(gain)):
            current_altitude=gain[i]+current_altitude
            max_altitude=max(max_altitude,current_altitude)

        return max_altitude

            