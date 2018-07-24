# Leetcode: https://leetcode.com/problems/maximize-distance-to-closest-person/description/

# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to closest person.

# Example 1:

# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:

# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Note:

# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.

# Be careful about testing cases
#  1. [1, 0]
#  2. [1, 0, 0] 
#  3. [0, 1]
#  4. [0, 1, 0, 0, 0, 1, 0]

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        l = len(seats)
        tracks = [0] * l 
        hasPerson = False
        personI = -1 # 0
        
        # From left to right
        for i in xrange(l):
            if seats[i]:
                hasPerson = True
                personI = i
            else:
                if hasPerson: # has person sitting on the left
                    tracks[i] = i - personI
                else: 
                    tracks[i] = float('inf')
        
        # From right to left
        hasPerson = False
        personI = -1
        for i in xrange(l-1, -1, -1):
            if seats[i]:
                hasPerson = True
                personI = i 
            else:
                if hasPerson: # has person sitting on the left
                    tracks[i] = min(tracks[i], personI - i) 
                else: 
                    tracks[i] = min(tracks[i], float('inf'))  
        
        curBest = float("-inf")
        for i in xrange(l):
            if curBest < tracks[i]:
                curBest = tracks[i]
                
        return curBest