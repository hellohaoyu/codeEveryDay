# Leetcode: https://leetcode.com/problems/wildcard-matching/description/

# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:

# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:

# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false

# m is the length of patten, space -- O(m)
# n is the length of word, time -- O(mn)
# DP[n] means if the match happens between s[:n] and p

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        DP = [ False for _ in xrange(len(s) + 1) ]
        DP[0] = True
        
        for pc in p:
            # update DP[1:]
            if pc == '*':
                for i in xrange(1, len(s) + 1):
                    DP[i] = DP[i-1] or DP[i]
            else:
                for i in reversed(xrange(1, len(s) + 1)): 
                    # Remember that, you want to use the old result and so you should start from l-1!!! Reverse comes in!
                    DP[i] = DP[i-1] and (pc == s[i-1] or pc == '?')
            # Update DP[0]
            DP[0] = DP[0] and pc == '*' # make DP[0] as true if you get * continuoustly!!
        return DP[-1]


# m is the length of patten, space -- O(mn)
# n is the length of word, time -- O(mn)
# DP[i][j] means if the match happens between s[:j] and p[:i]

# Love this better and it's clearer!!

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        DP = [ [False] * (len(s) + 1) for _ in xrange(len(p) + 1) ]
        DP[0][0] = True
        # init when s is empty!!
        for i in xrange(len(p)):
            if p[i] != "*":
                break
            DP[i+1][0] = True
        
        # check when we at least have 1 char in word, 1 char in patten
        for sI in xrange(1, len(s)+1):
            for pI in xrange(1, len(p) + 1): 
                if p[pI-1] == s[sI-1] or p[pI-1] == "?":
                    DP[pI][sI] = DP[pI-1][sI-1]
                elif p[pI-1] == "*":
                    DP[pI][sI] = DP[pI-1][sI-1] or DP[pI-1][sI] or DP[pI][sI-1]  # when it comes to * => 1. treat it as empty 2. replace the current char 3. leave it to next
        
        return DP[len(p)][len(s)]
                    