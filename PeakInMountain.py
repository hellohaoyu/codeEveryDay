# Leetcode: https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:

# Input: [0,1,0]
# Output: 1
# Example 2:

# Input: [0,2,1,0]
# Output: 1
# Note:

# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.


# Things should be careful:
# 1. Find mid from s + (e - s) / 2
# 2. Realized that the binary search would not work when there are duplicates [1,2,2,2,2,2, 6], because we can't decide which way to go.
#    Please ask clarification about that!!
# 3. Never miss the equal size for the while loop, otherwise, result will be missed for case : [0,2,1,0,-1].

class Solution(object):
    def peakIndexInMountainArray(self, A): 
        """
        :type A: List[int]
        :rtype: int
        """
        s = 0
        e = len(A) - 1
        
        while s <= e: # 0, 1 => Really important!!! Equal sign should be added., Case = [0,2,1,0,-1] failed when equal sign misses
            mid = s + (e - s) / 2 # 1
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid
            elif A[mid] > A[mid + 1] and A[mid] < A[mid - 1]:
                e = mid - 1 # 2 -1 = 1
            elif A[mid] < A[mid + 1] and A[mid] > A[mid - 1]:
                s = mid + 1
            else:
                print "Wrong input"
        
        return -1 # "Wrong input"


# Better solution with clearer idea!!
class Solution(object):
    def peakIndexInMountainArray(self, A): 
        """
        :type A: List[int]
        :rtype: int
        """
        s = 0
        e = len(A) - 1
        while s < e: 
            mid = s + (e - s) / 2 # 1
            if A[mid] < A[mid + 1]:
                s = mid + 1
            else:
                e = mid
        return s