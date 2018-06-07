# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Keys: 1. use iterator -- iter(list), next(iteratorObject) Nice!
#       2. Use list as rs and don't need to return list, otherwise there will be memory exceptions.

class Solution:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        rs = []
        self.serializeHelper(root, rs)
        
        return ",".join(rs)
    
    def serializeHelper(self, root, rs):
        if root:
            rs.append(str(root.val))
            self.serializeHelper(root.left, rs)
            self.serializeHelper(root.right, rs)  
        else:
            rs.append('#')
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        items = iter(data.split(','))
        
        return self.deserializeHelper(items)
    
    def deserializeHelper(self, items):
        val = next(items)
        if val == '#':
            return None
        root = TreeNode(int(val))
        root.left = self.deserializeHelper(items)
        root.right = self.deserializeHelper(items)
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))