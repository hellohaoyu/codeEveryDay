# Given a picture consisting of black and white pixels, find the number of black lonely pixels.

# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

# A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

# Example:
# Input: 
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]

# Output: 3
# Explanation: All the three 'B's are black lonely pixels.
# Note:
# The range of width and height of the input 2D array is [1,500].


# Naive solution one -- Two pass to get the number of blacks.
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture or not picture[0]:
            return 0
        
        lx = len(picture)
        ly = len(picture[0])
        vBlacks = [False] * lx
        hBlacks = [False] * ly
        
        for i in xrange(lx):
            if picture[i].count('B') == 1:
                vBlacks[i] = True
        
        for j in xrange(ly):
            count = 0
            for i in xrange(lx):
                if picture[i][j] == 'B':
                    count += 1
            if count == 1:
                hBlacks[j] = True
        
        rs = 0
        for i in xrange(lx):
            for j in xrange(ly):
                if vBlacks[i] and hBlacks[j] and picture[i][j] == 'B':
                    rs += 1
        
        return rs


# One pass to get the number of black in both row and column.
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture or not picture[0]:
            return 0
        
        lx = len(picture)
        ly = len(picture[0])
        vBlacks = [0] * lx
        hBlacks = [0] * ly
        
        for i in xrange(lx):
            for j in xrange(ly):
                if picture[i][j] == 'B':
                    vBlacks[i] += 1
                    hBlacks[j] += 1
        
        rs = 0
        for i in xrange(lx):
            for j in xrange(ly):
                if vBlacks[i] == 1 and hBlacks[j] == 1 and picture[i][j] == 'B':
                    rs += 1
        
        return rs