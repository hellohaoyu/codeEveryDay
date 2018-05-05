# Leetcode: https://leetcode.com/problems/find-peak-element/description/

# A peak element is an element that is greater than its neighbors.

# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that num[-1] = num[n] = -∞.

# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


import sys
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, -sys.maxint)
        nums.append(-sys.maxint)

# O(n) Solution        
#         for i in xrange(1, len(nums)):
#             if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
#                 return i-1

        s = 1
        e = len(nums) - 2
 
# binary search solution -> O(logn)        
        while e > s:
            c = (e + s) / 2
            if nums[c] > nums[c-1] and nums[c] > nums[c+1]:
                return c-1
            elif nums[c] > nums[c-1] and nums[c] < nums[c+1]:
                s = c + 1
            else:
                e = c - 1
        
        return e-1
    