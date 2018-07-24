# Leetcode: https://leetcode.com/problems/evaluate-division/description/

# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0. 
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

# Simplify version!!
from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        maps = defaultdict(set)
        valMaps = defaultdict(float)
        exists = set()
        for i in xrange(len(equations)):
            maps[equations[i][0]].add(equations[i][1])
            maps[equations[i][1]].add(equations[i][0])
            valMaps[(equations[i][0], equations[i][1])] = values[i]
            valMaps[(equations[i][1], equations[i][0])] = 1.0 / values[i]
            exists.update(equations[i])
        
        print valMaps
        rs = []
        for q in queries:
            if q[0] == q[1]:
                rs.append(1.0 if q[1] in exists else -1.0)
            else:
                rs.append(self.findPair(q, maps, valMaps))
        return rs
    
    def findPair(self, query, maps, valMaps):
        if self.DFS(set([query[0]]), 1.0, query[0], query[0], query[1], maps, valMaps):
            return valMaps[(query[0], query[1])] 
        return -1.0
         
    def DFS(self, visitedC, val, source, pre, target, maps, valMaps):
        if target in maps[pre]:
            valMaps[(source, target)] = val * valMaps[(pre, target)]
            return True
        
        for new in maps[pre]:
            if new not in visitedC:
                visitedC.add(new)
                newVal = val * valMaps[(pre, new)]
                if self.DFS(visitedC, newVal, source, new, target, maps, valMaps):
                    return True
                visitedC.remove(new)
        return False



# Previous version!!
from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        maps = defaultdict(set)
        valMaps = defaultdict(float)
        exists = set()
        for i in xrange(len(equations)):
            maps[equations[i][0]].add(equations[i][1])
            maps[equations[i][1]].add(equations[i][0])
            valMaps[(equations[i][0], equations[i][1])] = values[i]
            valMaps[(equations[i][1], equations[i][0])] = 1.0 / values[i]
            exists.update(equations[i])
        
        print valMaps
        rs = []
        for q in queries:
            if q[0] == q[1]:
                rs.append(1.0 if q[1] in exists else -1.0)
            else:
                rs.append(self.findPair(q, maps, valMaps))
        
        return rs
    
    def findPair(self, query, maps, valMaps):
        key = (query[0], query[1])
        if key in valMaps:  # Unnecessary -> Could be covered by DFS!
            return valMaps[key]
        
        self.DFS(set([query[0]]), 1.0, query[0], query[0], query[1], maps, valMaps)
        return valMaps[key] if key in valMaps else -1.0
        
        
    def DFS(self, visitedC, val, source, pre, target, maps, valMaps):
        if target in maps[pre]:
            valMaps[(source, target)] = val * valMaps[(pre, target)]
            return
        
        for new in maps[pre]:
            if new not in visitedC:
                visitedC.add(new)
                newVal = val * valMaps[(pre, new)]
                self.DFS(visitedC, newVal, source, new, target, maps, valMaps)  # Could stop earlier when return inside the DFS!!
                visitedC.remove(new)