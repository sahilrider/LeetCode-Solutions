'''https://leetcode.com/problems/check-if-it-is-a-straight-line/'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        '''
            y = mx+c
            Differentiating
            dy/dx = m
            Calculating m for each points and matching if it is same or not
        '''
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        dy = y1 - y0
        dx = x1 - x0
        for i in coordinates[2:]:
            dxi = i[0] - x0
            dyi = i[1] - y0
            if dy*dxi != dyi*dx:
                return False
        return True