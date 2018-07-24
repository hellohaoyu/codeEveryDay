# Leetcode: https://leetcode.com/problems/task-scheduler/description/

# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

from collections import defaultdict
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        mapTasks = defaultdict(int)
        for t in tasks:
            mapTasks[t] += 1
        
        maxVal = 0
        maxC = 0
        for t, val in mapTasks.iteritems():
            if maxVal == val:
                maxC += 1
            elif maxVal < val:
                maxVal = val
                maxC = 1            
        atLeast = maxVal + (maxVal - 1) * n + maxC - 1 # We only care about the tasks with max number , which gives us the least estimations.
        if len(tasks) <= atLeast: 
            return atLeast
        return len(tasks)