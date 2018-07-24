# Leetcode: https://leetcode.com/problems/the-maze/description/

# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

# How to write clean code:  put visited set at the beginning of the helper method.

class Solution(object):
    DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        visited = [ [False] * len(maze[0]) for i in xrange(len(maze)) ]
        self.helper(start[0], start[1], visited, maze)
        
        return visited[destination[0]][destination[1]]
    
    def helper(self, r, c, visited, maze):
        visited[r][c] = True  # Right place to add
        for d in self.DIRS:
            tempR = r
            tempC = c
            while self.isNotWall(maze, tempR + d[0], tempC + d[1]):
                tempR += d[0]
                tempC += d[1]
            if not visited[tempR][tempC]:
                self.helper(tempR, tempC, visited, maze) 
    
    def isNotWall(self, maze, r, c):
        return r >= 0 and c >= 0 and r < len(maze) and c < len(maze[0]) and maze[r][c] == 0