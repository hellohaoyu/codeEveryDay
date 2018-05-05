# Leetcode: https://leetcode.com/problems/first-unique-character-in-a-string/description/

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


# Be careful about what you will store in the list.
# Start testing from simple examples, such as 'l' and 'lal'


# One pass idea
import sys
class Solution(object):
    OFFSET =  ord('a')
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapChar = [-1] * 26
        
        for i in range(len(s)):
            mI = ord(s[i]) - self.OFFSET
            if mapChar[mI] == -1:
                mapChar[mI] = i
            elif mapChar[mI] == -2:
                continue
            else:
                mapChar[mI] = -2
        rs = sys.maxint
        for i in xrange(26):
            if mapChar[i] > -1 and rs > mapChar[i]:
                rs = mapChar[i]
        
        return rs if rs != sys.maxint else -1



# Two pass ideas
class Solution(object):
    OFFSET =  ord('a')
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapChar = [0] * 26
        
        for i in range(len(s)):
            mI = ord(s[i]) - self.OFFSET
            mapChar[mI] += 1
        
        
        for i in range(len(s)):
            mI = ord(s[i]) - self.OFFSET
            if mapChar[mI] == 1:
                return i
        
        return -1