# Leetcode: https://leetcode.com/problems/new-21-game/description/

# Alice plays the following game, loosely based on the card game "21".

# Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

# Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

# Example 1:

# Input: N = 10, K = 1, W = 10
# Output: 1.00000
# Explanation:  Alice gets a single card, then stops.
# Example 2:

# Input: N = 6, K = 1, W = 10
# Output: 0.60000
# Explanation:  Alice gets a single card, then stops.
# In 6 out of W = 10 possibilities, she is at or below N = 6 points.
# Example 3:

# Input: N = 21, K = 17, W = 10
# Output: 0.73278

# Points:
#   1. Relize how to calculate the next probability -- (sum of previous k seneraios) / w  
#   2. Realize the final situations would be k, k+1, ...., k + w - 1


class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0 or N >= K + W - 1:
            return 1.0
        dp = [1.0] + [0.0] * N
        
        sumUp = 1.0
        for i in xrange(1, N+1):
            dp[i] = sumUp / W
            if i < K:
                sumUp += dp[i]
            if i >= W:
                sumUp -= dp[i-W]
        
        return sum(dp[K:])   