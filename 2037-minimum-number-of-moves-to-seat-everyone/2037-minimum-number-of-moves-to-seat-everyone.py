class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        students.sort()
        seats.sort()
        moves=0
        for i in range(len(seats)):
            moves+=abs(students[i]-seats[i])
        return moves
