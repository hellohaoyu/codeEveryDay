# Leetcode: https://leetcode.com/problems/plus-one/

# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits): # [1,9]
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return digits
    
        p = len(digits) - 1
        carry = 1
        
        while carry and p >= 0:
            curD = digits[p]
            newD = curD + carry
            digits[p] = newD % 10
            
            if newD <= 9: 
                return digits
            
            carry = newD / 10
            p -= 1
        
        if carry:
            digits.insert(0, carry)
        
        return digits 


# Simplify methods -- Take advantage of only plusing one
class Solution(object):
    def plusOne(self, digits): # [1,9]
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return digits
        
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        digits.insert(0, 1)
        return digits        