class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        m1_num = coordinates[1][1] - coordinates[0][1]
        m1_den = coordinates[1][0] - coordinates[0][0]
        if m1_den == 0:
            m1 = None
        else:
            m1 = m1_num/m1_den
        for i in range(1, len(coordinates)-1):
            m2_num = coordinates[i+1][1] - coordinates[i][1]
            m2_den = coordinates[i+1][0] - coordinates[i][0]
            if m2_den == 0:
                m2 = None
            else:
                m2 = m2_num/m2_den
            if m1!= m2:
                return False
        return True