# Leetcode: https://leetcode.com/problems/find-the-celebrity/description/

# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

# Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.


# Simple Test cases: 
# 1. 0 knows 1, but  1 doesn't know 0  -> 1 is celebrity 
# 2. 0 knows 1, 1 knows 0   
# 3. 1 doesn't know 0, 0 doesn't know 1.

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur = 0
        for i in xrange(1, n):  # Idea to find the possible candidate
            if knows(cur, i):
                cur = i
            
        for i in xrange(n):
            if cur != i and (knows(cur, i) or not knows(i, cur)):  # Be careful of not missing one condition!!
                return -1            
        
        return cur

# Other: you could also use O(n^2) naive method. but for here, O(1) space, O(n) time