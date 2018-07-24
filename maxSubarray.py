# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curBest = nums[0]
        globalBest = nums[0]
        for n in nums[1:]:
            if curBest > 0:
                curBest += n
            else:
                curBest = n
            globalBest = max(globalBest, curBest)
        return globalBest



# Divide and conquor solution!!
class Result(object):
    def __init__(self, leftBest, rightBest, best, totalSum):
        self.leftBest = leftBest
        self.rightBest = rightBest
        self.best = best
        self.totalSum = totalSum

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = self.getResult(nums, 0, len(nums))
        return result.best
    
    def getResult(self, nums, s, e):
        if e - s <= 1:
            return Result(nums[s], nums[s], nums[s], nums[s])
        leftResult = self.getResult(nums, s, s + (e - s) / 2) # remember to update the index in right way!!! Don't use the lenght of list.!!
        rightResult = self.getResult(nums, s + (e - s) / 2, e)
        
        leftBest = max(leftResult.leftBest, leftResult.totalSum + rightResult.leftBest)
        rightBest = max(rightResult.rightBest, rightResult.totalSum + leftResult.rightBest)
        best = max(max(rightResult.best, leftResult.best), rightResult.leftBest + leftResult.rightBest)
        totalSum = leftResult.totalSum + rightResult.totalSum
        
        return Result(leftBest, rightBest, best, totalSum)