# Leetcode: https://leetcode.com/problems/single-element-in-a-sorted-array/description/

# Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return reduce(lambda x, y: x ^ y, nums)
        s = 0
        e = len(nums) - 1
        while s < e:
            mid = s + (e - s) / 2
            if nums[mid] == nums[mid - 1]:
                if mid % 2:
                    s = mid + 1
                else:
                    e = mid - 1
            elif nums[mid] == nums[mid + 1]:
                if mid % 2:
                    e = mid - 1
                else:
                    s = mid + 1 
            elif nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
        return nums[s]