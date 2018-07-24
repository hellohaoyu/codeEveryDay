# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# 1. Insert a character
# 2. Delete a character
# 3. Replace a character

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

# Key 1: Remember to use the right dynamic programming array
#      use 2 D array the width and height are from the lengths of two input words.
# key 2: Please be really careful about the four senerios:
#      a. two chars are the same b. different char  c. delete word1 char d. delete word2 char.

class Solution(object):
    def minDistance(self, word1, word2): # a, b
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        DP = [ [0] * (l1 + 1) for i in xrange(l2 + 1) ]
        for i in xrange(1, l1 + 1):
            DP[0][i] = i
        for j in xrange(1, l2 + 1):
            DP[j][0] = j
        
        for i in xrange(1, l1 + 1):
            for j in xrange(1, l2 + 1):
                DP[j][i] = min(DP[j-1][i] + 1, DP[j][i-1] + 1)
                if word1[i-1] == word2[j-1]:
                    DP[j][i] = min(DP[j][i], DP[j-1][i-1])
                else:
                    DP[j][i] = min(DP[j][i], DP[j-1][i-1] + 1)
        return DP[l2][l1]