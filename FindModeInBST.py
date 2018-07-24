# Leetcode: https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# For example:
# Given BST [1,null,2,2],
#    1
#     \
#      2
#     /
#    2
# return [2].

# Note: If a tree has more than one mode, you can return them in any order.

# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(n) space
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = {}
        self.helper(root, vals)
        
        rs = []
        maxNum = 0
        for key in vals.keys():
            if vals[key] == maxNum:
                rs.append(key)
            elif vals[key] > maxNum:
                maxNum = vals[key]
                rs = [key]
        
        return rs
            
    def helper(self, root, vals):
        if not root:
            return
        self.helper(root.left, vals)
        if root.val in vals:
            vals[root.val] += 1
        else:
            vals[root.val] = 1
        self.helper(root.right, vals)


# O(1) space! -- Be careful!

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.rs = []
        self.maxCount = 1
        self.count = 1
        self.preV = None
        self.helper(root)
        
        return self.rs
    
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        if root.val != self.preV:  # Check the count firstly!!
            self.count = 1
            self.preV = root.val
        else:
            self.count += 1
            
        if self.maxCount < self.count:  # Update the result later!! seperatately.
            self.maxCount = self.count
            self.rs = [root.val]
        elif self.maxCount == self.count:
            self.rs.append(root.val)
            
        self.helper(root.right)
        
        