# Leetcode: https://leetcode.com/problems/trapping-rain-water/description/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# The major idea is to focus one position and check the leftMax and rightMax and then get value [min(rightMax, leftMax) - curVal] 

# Solution one: Store right most with a list

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        rs = 0
        if l == 0 or l == 1:
            return rs
        
        rightMax = []
        curRightMax = 0
        for i in reversed(xrange(l)):
            curRightMax = max(height[i], curRightMax)
            rightMax.insert(0, curRightMax)
        
        curLeftMax = 0
        for i in xrange(l):
            curLeftMax = max(curLeftMax, height[i])
            baseV = min(curLeftMax, rightMax[i])
            if baseV > height[i]:
                rs += baseV - height[i]
        
        return rs


# Divide the list into two parts -> the elements on the right of tallest and the ones on the left of tallest.
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        rs = 0
        if l == 0 or l == 1:
            return rs
        
        tallest = 0
        for i in xrange(l):
            if height[i] > height[tallest]:
                tallest = i
        
        # the left elements of tallest position
        leftMax = 0
        for i in xrange(tallest):
            if leftMax < height[i]:
                leftMax = height[i]
            else:
                rs += leftMax - height[i]
        
        rightMax = 0
        for i in reversed(xrange(tallest+1, l)):
            if rightMax < height[i]:
                rightMax = height[i]
            else:
                rs += rightMax - height[i]
        
        return rs