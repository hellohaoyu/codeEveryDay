# Given an encoded string, return it's decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

# Key: 
#   1. Convert the string into a list with number and str group well.
#   2. Now if you are sure about the pattern, then get list of strings and get the times.

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = 0
        proS = []
        while p < len(s):
            if s[p] in '[]':
                proS.append(s[p])
                p += 1
            elif s[p].isalpha():
                newS = []
                while p < len(s) and s[p].isalpha():
                    newS.append(s[p])
                    p += 1
                proS.append("".join(newS)) 
            else:
                newD = []
                while p < len(s) and s[p].isdigit():
                    newD.append(s[p])
                    p += 1
                proS.append("".join(newD))
        stack = []     
        for c in proS:
            if c == ']':
                newS = []
                while stack and stack[-1].isalpha():
                    newS.append(stack.pop())
                stack.pop() # pop up "["
                times = int(stack.pop()) # pop up number
                strs = "".join(reversed(newS)) # Need to be reversed!
                stack.append(times * strs)
            else:
                stack.append(c)
        return "".join(stack)