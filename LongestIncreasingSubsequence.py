# Leetcode: https://leetcode.com/problems/longest-increasing-subsequence/description/
# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?


# O(n^2 solution) --> Get solution from (n-1) subsolutions.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        tempPairs = [1] * len(nums)
        rs = 0
        for eI in xrange(1, len(nums)):
            for sI in xrange(eI):
                if nums[eI] > nums[sI]:
                    tempPairs[eI] = max(tempPairs[eI], tempPairs[sI] + 1)
        return max(tempPairs)


# Because we only care about the number of list.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sortedNums = [nums[0]]
        for i in xrange(1, len(nums)):
            if nums[i] > sortedNums[-1]:
                sortedNums.append(nums[i])
            else:
                swapIndex = self.binarySearch(sortedNums, nums[i])
                sortedNums[swapIndex] = nums[i]
        return len(sortedNums)
                
    def binarySearch(self, nums, val): # Get the index of value who is the smallest one to larger or equal to the input val 
        s = 0
        e = len(nums) - 1
        while s < e:
            mid = s + (e - s) / 2
            if nums[mid] == val:
                return mid
            elif nums[mid] > val:
                e = mid - 1
            else:
                s = mid + 1 
                
        while nums[s] < val:
            s += 1
        return s