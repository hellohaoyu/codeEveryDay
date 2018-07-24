# https://leetcode.com/problems/spiral-matrix-ii/description/

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


# Basically idea is to generate a squence of new positions and then assign the val

class Solution(object):
    DIRS = [[0, 1], [1, 0], [0, -1]]
    upDir = [-1, 0]
    leftDir = [0, 1] 
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rs = [[0] * n for i in xrange(n)]
        x, y = 0, 0
        steps = n - 1 
        rs[x][y] = 1
        s = 2  # Key to start from 2
        end = n*n
        while s < end:
            q = []
            x, y, steps = self.getQueue(x, y, steps, q)
            for pair in q:
                rs[pair[0]][pair[1]] = s
                s += 1
        return rs
    
    def getQueue(self, x, y, steps, queue):
        for d in self.DIRS:   # Three normal direction!
            for i in xrange(steps):
                x += d[0]
                y += d[1]
                queue.append((x, y))
                
        for i in xrange(steps - 1):  # Up special direction
            x += self.upDir[0]
            y += self.upDir[1]
            queue.append((x, y)) 
            
        if steps - 1 > 0:  # Only need to move one step if there is space
            x += self.leftDir[0]
            y += self.leftDir[1]
            queue.append((x, y)) 
        
        return x, y, steps - 2  # remember to reduce the number of steps by 2!