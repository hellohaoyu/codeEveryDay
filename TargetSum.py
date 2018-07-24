# Leetcode: https://leetcode.com/problems/target-sum/description/

# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.


# 1. Think of divide and conquer when it comes to the problem of naive solution 2^n to O(n^3)

from collections import defaultdict
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.helper(nums, 0, len(nums) - 1)[S]
        
    def helper(self, nums, sI, eI):
        maps = defaultdict(int)
        if sI == eI:
            maps[nums[sI]] += 1
            maps[-nums[sI]] += 1
            return maps

        mid = sI + (eI - sI) / 2
        leftHash = self.helper(nums, sI, mid)
        rightHash = self.helper(nums, mid+1, eI)
        
        for lkey, lval in leftHash.iteritems():
            for rkey, rval in rightHash.iteritems():
                maps[lkey+rkey] += lval * rval
        return maps


# Find the DP solution with O(K) space and O(nk) time, k is the sum of all the nums.
from collections import defaultdict
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sumV = reduce(lambda a, b: a + b, nums)  # Use reduce!!
        if S > sumV or S < -sumV or not nums:
            return 0
        DP = [0] * (2*sumV + 1) # Set the right size of array DP!
        DP[sumV + nums[0]] += 1 # Be careful about the init!!
        DP[sumV - nums[0]] += 1
            
        for num in nums[1:]:
            newDP = [0] * (2*sumV + 1)
            for p, c in enumerate(DP):
                if c:
                    newDP[p - num] += c
                    newDP[p + num] += c
            DP = newDP
        return DP[S + sumV]