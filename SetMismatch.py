# Leetcode Link: https://leetcode.com/problems/set-mismatch/description/

# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.

# Be careful about what value should be switched.
# Testing cases: 1. [2, 3, 2] => [1,2], 2.[1, 2, 2, 4] => [2,3]
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = sum(nums)
        for i in xrange(1, len(nums) + 1):
             diff -= i
        
        duplicateNum = 0
        for p in xrange(len(nums)): 
            while nums[p] != p+1:
                val = nums[p]
                if nums[val-1] == val:
                     return [val, val - diff]       
                nums[p] = nums[val - 1]
                nums[val-1] = val