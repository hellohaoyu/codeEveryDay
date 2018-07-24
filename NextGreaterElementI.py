# Leetcode: https://leetcode.com/problems/next-greater-element-i/description/

# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the second array is 3.
#     For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
# Note:
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.

# Similar as https://leetcode.com/problems/daily-temperatures/, it's to get the first value that is greater than target.

# The idea is that  num[i] > num[i+1], then we  need to jump to check the number larger than num[i+1]

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        valOffSet = [0] * len(nums)
        for i in xrange(len(nums) - 2, -1, -1):
            nextI = i+1
            while nums[i] > nums[nextI]:
                if valOffSet[nextI] == 0:
                    nextI = i
                    break
                else:
                    nextI += valOffSet[nextI]
            valOffSet[i] = nextI - i
            
        rs = []
        for num in findNums:
            i = nums.index(num)
            if valOffSet[i]:
                rs.append(nums[i + valOffSet[i]])
            else:
                rs.append(-1)
        return rs