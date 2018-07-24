# Leetcode: https://leetcode.com/problems/queue-reconstruction-by-height/description/

# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.


# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


# Think about how to generating the list -> Trick -> sort based on both heigh and number of person ahead, and then starting from the highest to put.

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def comFun(p1, p2):  # Reversed order. So p2[0] - p1[0]
            if p1[0] != p2[0]:
                return  p2[0] - p1[0]
            else:
                return p1[1] - p2[1]
        people.sort(cmp = comFun)
        
        rs = []
        
        for p in people:
            if p[1] == len(rs):
                rs.append(p)
            else:
                rs.insert(p[1], p)
        
        return rs  