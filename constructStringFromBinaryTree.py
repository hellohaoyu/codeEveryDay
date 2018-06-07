# Leetcode: https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /    
#   4     

# Output: "1(2(4))(3)"

# Explanation: Originallay it needs to be "1(2(4)())(3()())", 
# but you need to omit all the unnecessary empty parenthesis pairs. 
# And it will be "1(2(4))(3)".

# Input: Binary tree: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \  
#       4 

# Output: "1(2()(4))(3)"

# Explanation: Almost the same as the first example, 
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Be careful about the rules => root(Left)(Right) when both left and right exists.

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        rs = str(t.val)
        if t.left and t.right:
            return rs + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"
        elif t.left:
            return rs + "(" + self.tree2str(t.left) + ")"
        elif t.right:
            return rs + "()(" + self.tree2str(t.right) + ")"  # Remember to check the needs!!! rootVal(Left)(Right)
        else:
            return rs