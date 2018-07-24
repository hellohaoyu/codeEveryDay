# Leetcode: https://leetcode.com/problems/positions-of-large-groups/description/

# In a string S of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

# The final answer should be in lexicographic order.

 

# Example 1:

# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# Example 2:

# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# Example 3:

# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]


# More elegant solution with less variables.
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        rs = []
        if not S:
            return rs
        
        l = len(S) 
        p1 = 0
        p2 = 0
        while p1 < l:
            while p2 < l and S[p1] == S[p2]:
                p2 += 1
            
            if p2 - p1 >= 3:
                rs.append([p1, p2 - 1])
            p1 = p2
        
        return rs   


# My init solution
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        rs = []
        if not S:
            return rs
        
        l = len(S)
        p = 1
        cur = S[0]
        count = 1
        while p < l:
            if cur == S[p]: # 
                count += 1
            else:
                if count >= 3:
                    rs.append([p - count, p -1])
                count = 1
                cur = S[p]
            p += 1
        
        if count >= 3:  # Don't forget this. If you use method one, no special case needs to be dealed with.
            rs.append([p - count, p -1])
        
        return rs