# Leetcode: https://leetcode.com/problems/valid-parentheses/

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


# Better solution: It stops earlier
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif stack: # stack not s
                if (c == ')'and stack[-1] == '(') or (c == ']'and stack[-1] == '[') or (c == '}'and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False  # Be careful when to return False
            else:
                return False # Be careful when to return False
        
        if not stack: # Never miss this case!!
            return True
        
        return False    


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif (c in dict) and (dict[c] == stack[-1]):
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0 