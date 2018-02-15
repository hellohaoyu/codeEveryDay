# https://leetcode.com/problems/add-strings/description/

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

import collections

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        c = 0
        rs = ""
        
        while l1 > 0 or l2 > 0:
            d1 = 0
            d2 = 0
            if l1 > 0:
                d1 = int(num1[l1 - 1])
                l1 -= 1
            if l2 > 0:
                d2 = int(num2[l2 - 1])
                l2 -= 1
            newD = c + d1 + d2
            if newD >= 10:
                newD %= 10
                c = 1
            else:
                c = 0
            
            rs = str(newD) + rs
        
        if c == 1:
            rs = '1' + rs
        
        return rs 

    def addStringsWithDeque(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        c = 0
        rs = collections.deque()  # It's better to use deque when requiring appending element from left.
        
        while l1 > 0 or l2 > 0:
            d1 = 0
            d2 = 0
            if l1 > 0:
                d1 = int(num1[l1 - 1])
                l1 -= 1
            if l2 > 0:
                d2 = int(num2[l2 - 1])
                l2 -= 1
            newD = c + d1 + d2
            if newD >= 10:
                newD %= 10
                c = 1
            else:
                c = 0
            rs.appendleft(str(newD))
        
        if c == 1:
            rs.appendleft('1')
        
        return "".join(rs)



s = Solution()

print s.addStrings("1", "999999")
print s.addStrings("12", "123299")


print s.addStringsWithDeque("1", "999999")
print s.addStringsWithDeque("12", "123299")
