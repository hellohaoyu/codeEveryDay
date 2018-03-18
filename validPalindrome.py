# Leetcode: https://leetcode.com/problems/valid-palindrome/description/

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.

class Solution(object):
    CHARS = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def isPalindrome(self, s): # 0P
        """
        :type s: str
        :rtype: bool
        """
        p1 = 0
        p2 = len(s) - 1 # 1
        
        
        while p1 < p2: # 0 < 1
            if s[p1] not in self.CHARS:
                p1 += 1
                continue
            if s[p2] not in self.CHARS:
                p2 -= 1
                continue
            
            if ord(s[p1].lower()) != ord(s[p2].lower()):
                return False
            p1 += 1
            p2 -= 1
        
        return True