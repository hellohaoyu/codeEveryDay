# https://leetcode.com/problems/longest-mountain-in-array/description/

# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)

# Given an array A of integers, return the length of the longest mountain. 

# Return 0 if there is no mountain.

# Example 1:

# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
# Note:

# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# Follow up:

# Can you solve it using only one pass?
# Can you solve it in O(1) space?

# Testing cases:
# 1. [1,2,3]  2.[3,2,1] 3.[1,2,1] 4.[2,1,4,7,3,2,5]

# Best solution -- starting from peak!! Clear and elegant!! My idea!
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        best = 0
        if not A:
            return best
        l = len(A)
        if l < 3:
            return best
        
        for i in xrange(1, l-1):
            if self.isPeak(A, i):
                best = max(best, self.getMountainLen(A, i))
        return best
    
    def isPeak(self, nums, i):
        return nums[i] > nums[i-1] and nums[i] > nums[i+1]
    
    def getMountainLen(self, nums, i):
        left = i
        countLeft = 0
        while left > 0 and nums[left] > nums[left-1]:
            countLeft += 1
            left -=1
            
        right = i
        countRight = 0
        l = len(nums)
        while right < l-1 and nums[right] > nums[right+1]:
            countRight += 1
            right += 1
        
        return countRight + countLeft + 1

# Instead of remembering index, we would like to memeorize just up and down count!! index will have too much extra effor.
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        best = 0
        if not A:
            return best
        l = len(A)
        if l < 3:
            return best
        
        p = 0
        up = 0
        down = 0
        while p < l-1:
            if down == 0:
                if A[p] < A[p+1]:
                    up += 1
                elif A[p] == A[p+1]:
                    up = 0
                elif A[p] > A[p+1] and up > 0:
                    down += 1
            else:
                if A[p] > A[p+1]:
                    down += 1
                elif A[p] == A[p+1]:
                    best = max(best, up + down + 1)
                    up = 0
                    down = 0
                else:
                    best = max(best, up + down + 1)
                    up = 1
                    down = 0
            p += 1
        
        if down > 0:
            best = max(best, up + down + 1)
        
        return best


# The first naive solution, but just check the start index and then search for  upperHill, downhill, one by one!!
# This method is easy to make mistake and hard to explain. Tons of details to be careful.
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        best = 0
        if not A:
            return best
        l = len(A)
        if l < 3:
            return best
        
        p = 0
        while p < l-1: # 0 < 2
            if A[p] >= A[p+1]:
                p += 1
                continue

            # Search for upper hill
            startIndex = -1
            while A[p] < A[p+1]: # A[0] > A[1]
                if startIndex == -1:
                    startIndex = p
                p += 1
                if p >= l-1:
                    return best
            # Stop when having flat in the middle
            if A[p] == A[p+1]:
                p += 1
                continue
            
            # Search for downhill
            while A[p] > A[p+1]:
                p += 1
                if p >= l-1:
                    best = max(best, p - startIndex + 1)
                    return best
            
            best = max(best, p - startIndex + 1)
        
        return best
