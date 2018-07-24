# Leetcode: https://leetcode.com/problems/bus-routes/description/

# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

# We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

# Example:
# Input: 
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation: 
# The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Note:

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.

# 1. Typical BFS method
# 2. Remember to set the bus rounte to be empty after it has been visited!! Otherwise, it will be time-out!


from collections import defaultdict
from collections import deque
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        stopToBuses = defaultdict(set)
        for bus in xrange(len(routes)):
            for stop in routes[bus]:
                stopToBuses[stop].add(bus)
        count = 0
        q = deque([])
        q.append(S)
        visited = set()
        
        while q:
            l = len(q)
            for i in xrange(l):
                curStop = q.popleft()
                if curStop == T:
                    return count
                visited.add(curStop)
                for bus in stopToBuses[curStop]:
                    for stop in routes[bus]:
                        if stop not in visited:
                            q.append(stop)
                    routes[bus] = [] # Really really important!!!           
            count += 1
        return -1