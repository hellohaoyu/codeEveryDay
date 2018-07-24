# Leetcode: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in xrange(len(nums)):
            while nums[i] != i+1 and nums[nums[i] - 1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[temp - 1]   # Be really careful about the nums[i], please use temp
                nums[temp - 1] = temp
            # while nums[i] != i+1 and nums[nums[i] - 1] != nums[i] - 1:  # Error 1: wrong value checking!!
            #     temp = nums[i]
            #     nums[i] = nums[nums[i] - 1] # without aware of the change of nums[i], should use temp!
            #     nums[nums[i] - 1] = temp
        
        rs = []
        for i in xrange(len(nums)):
            if nums[i] != i+1:
                rs.append(i+1)
        
        return rs
        