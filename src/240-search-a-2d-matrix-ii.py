'''https://leetcode.com/problems/search-a-2d-matrix-ii/'''

import numpy as np
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[] or matrix==[[]]:
            return False
        i, j =  0, len(matrix[0]) -1
        while i<len(matrix) and j>-1:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return False

###########################
# Divide n Conquer
###########################
import numpy as np
class Solution:
    def dnc(self, matrix, target, startm, startn, endm, endn):
        midm, midn = (startm+endm)//2, (startn+endn)//2
        if startm>endm or startn>endn:
            return False
        if matrix[midm][midn]==target:
            return True
        elif matrix[midm][midn]>target:
            return self.dnc(matrix, target, startm, startn, midm-1, midn-1) or \
                   self.dnc(matrix, target, startm, midn-1, midm-1, endn) or \
                   self.dnc(matrix, target, midm, startn , endm, midn-1)
        else:
            return self.dnc(matrix, target, midm+1, midn+1, endm, endn) or \
                   self.dnc(matrix, target, startm, midn+1, midm, endn) or \
                   self.dnc(matrix, target, midm+1, startn , endm, midn)
        
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[] or matrix==[[]]:
            return False
        return self.dnc(matrix, target, 0, 0, len(matrix)-1, len(matrix[0])-1)