# Leetcode: https://leetcode.com/problems/course-schedule/description/

# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


# Classical topological sorting algorithm!!
# Remember to maintain two O(n) space structure:
#   1. Visited nodes (The ones which have been proved to not be part of circle)
#   2. Visiting notes (The ones which form current path)

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [False] * numCourses
        courseMap = {}
        for pair in prerequisites:
            if pair[1] not in courseMap:
                courseMap[pair[1]] = [pair[0]]
            else:
                courseMap[pair[1]].append(pair[0])
                
        for i in xrange(numCourses):
            if not visited[i] and self.hasCircle(visited, set(), i, courseMap):
                return False
        
        return True
    
    def hasCircle(self, visited, visiting, curC, courseMap):
        if visited[curC]:  # The order of if statement matter!!!
            return False
        if curC in visiting: 
            return True
        visiting.add(curC)
        if curC in courseMap:
            for nextC in courseMap[curC]:
                if self.hasCircle(visited, visiting, nextC, courseMap):
                    return True
        visited[curC] = True
        return False

# More realistic solution while interviewing!!
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [False] * numCourses
        courseMap = defaultdict(list)
        for pre in prerequisites:
            courseMap[pre[1]].append(pre[0]) # key: pre, val: nexts
        
        for c in xrange(numCourses):
            if not visited[c] and self.DFS(c, set(), visited, courseMap):
                return False
        return True
                
    
    def DFS(self, curC, visiting, visited, courseMap):
        if curC in visiting:
            return True
        visiting.add(curC)
        visited[curC] = True
        for nextC in courseMap[curC]:
            if self.DFS(nextC, visiting, visited, courseMap):
                return True
            visiting.remove(nextC)
                
        return False