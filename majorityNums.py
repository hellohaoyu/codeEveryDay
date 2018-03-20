# Leetcode: https://leetcode.com/problems/majority-element/description/

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# The trick is to use majority vote algorithm. 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majorNum = nums[0]
        count = 1
        for i in xrange(1, len(nums)):
            if count == 0:
                majorNum = nums[i]
                count = 1
            elif nums[i] == majorNum:
                count += 1
            elif nums[i] != majorNum:
                count -= 1
        
        return majorNum