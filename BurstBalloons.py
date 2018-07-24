# Leetcode: https://leetcode.com/problems/burst-balloons/description/

# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons wisely.

# Note:

# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:

# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


# Key -- 1. Use the divide and conquer and realize that after bursting a ballnoon, it basically, divide the problem into two parts
#        2. We need to grow the solution from the length of 3 (single element) into n

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(1)
        nums.insert(0, 1)
        l = len(nums)
        DP = [ [0] * l for i in xrange(l) ]
        for inc in xrange(2, l):
            for i in xrange(l-inc):
                startI = i
                endI = i+inc
                left = nums[startI]
                right = nums[endI]
                for burnI in xrange(startI+1, endI):
                    curVal = left * nums[burnI] * right + DP[startI][burnI] + DP[burnI][endI]
                    DP[startI][endI] = max(DP[startI][endI], curVal)
        return DP[0][l-1]