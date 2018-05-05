# Leetcode: https://leetcode.com/problems/one-edit-distance/description/

# Given two strings S and T, determine if they are both one edit distance apart.

# Only contains delete one, add one, replace one (Not include swap one)

# Key: 
#    1. Never miss the case when s and t are equal
#    2. Realize that addOne is the same as deleteOne. Only need to swap s and t. 

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tl = len(t)
        sl = len(s)
        
        if tl == sl:
            return self.checkNeedReplaceOne(s, t)
        elif tl - sl == 1:
            return self.checkNeedAddOne(s, t)
        elif sl - tl == 1:
            return self.checkNeedDeleteOne(s, t)
        
        return False
    
    def checkNeedReplaceOne(self, s, t):
        numOneDiff = False
        for i in xrange(len(s)): # 3
            if s[i] != t[i]: # True
                if not numOneDiff:#
                    numOneDiff = True #
                else:
                    return False
        return numOneDiff

    def checkNeedAddOne(self, s, t):
        sp = 0
        tp = 0
        canAddOne = True
        while sp < len(s): # 3
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                if canAddOne:
                    tp += 1
                    canAddOne = False
                else:
                    return False
        return True      
    
    # Realize delete one and add one is the same thing!!!
    def checkNeedDeleteOne(self, s, t):
        return self.checkNeedAddOne(t, s)


            