# Leetcode: https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/

# You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False

# Key: 1. maintain two maps -> nums counter map, consective ending maps
# Update cases: 1. zero for adding 2. Has ending to connected 3. Could create new one! 4. Error!!


from collections import defaultdict
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsMap = defaultdict(int)
        for n in nums:
            numsMap[n] += 1
        tempMaps = defaultdict(int)
        
        for n in nums:
            if numsMap[n] == 0:
                continue
            numsMap[n] -= 1 
            if tempMaps[n-1] > 0:
                tempMaps[n] += 1
                tempMaps[n-1] -= 1
            elif numsMap[n+1] > 0 and numsMap[n+2] > 0:
                tempMaps[n+2] += 1
                numsMap[n+1] -= 1 
                numsMap[n+2] -= 1
            else:
                return False
        return True