# Leetcode: https://leetcode.com/explore/interview/card/google/61/trees-and-graphs-2/437/

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Notes:
#    1. Find a complete testing case:
#                       10
#                    2     13
#                 -2   8

#    2. Remember to make sure return false when there are nodes with same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        q = [root]
        preVal = -sys.maxint - 1
        visited = set()
        
        while q:
            cur = q[-1]
            if cur in visited:
                q.pop()
                continue
            if cur.left and cur.left not in visited:
                q.append(cur.left)
            else:
                if preVal >= cur.val:
                    return False
                preVal = cur.val
                visited.add(cur)
                if cur.right:
                    q.append(cur.right)
            
        return True
                