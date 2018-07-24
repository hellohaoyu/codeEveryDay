# Leetcode: https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

# Example:

# Input:

#    1
#     \
#      3
#     /
#    2

# Output:
# 1

# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    minDiff = float('inf')
    preNode = None
    def getMinimumDifference(self, root):
        if not root:
            return self.minDiff
        
        self.getMinimumDifference(root.left)
        if self.preNode:
            self.minDiff = min(self.minDiff, abs(root.val - self.preNode.val))
        self.preNode = root
        self.getMinimumDifference(root.right)
        
        return self.minDiff




# Node: Bad solution below -- You don't need to create a helper method for it. Just use itself for recursion!

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    minDiff = float('inf')
    preNode = None
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.minDiff = float('inf')
        self.preNode = None
        self.helper(root)
        
        return self.minDiff
    
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        if self.preNode:
            self.minDiff = min(self.minDiff, abs(root.val - self.preNode.val))
        self.preNode = root
        self.helper(root.right)