# Leetcode Link -- https://leetcode.com/problems/find-the-difference/description/

# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Find the letter that was added in t.

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # Testing case 1: "a", "ab"
        # Testing case 2: "a", "aa"  -> Missing!!!
        # Testing case 3: "abc", "bdca"
        charMap = {}
        for sC in s:
            if sC in charMap:
                charMap[sC] += 1 
            else:
                charMap[sC] = 1
                
        for tC in t:
            if tC not in charMap:
                return tC
            else:
                charMap[tC] -= 1
                if charMap[tC] < 0:
                    return tC

class SolutionTwo(object):
    BASE_LOWER_CASE_UNICODE = ord('a')
    NUM_OF_CHARS = 26 
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # Testing case 1: "a", "ab"
        # Testing case 2: "a", "aa"  -> Missing!!!
        # Testing case 3: "abc", "bdca"
        charMap = [0] * self.NUM_OF_CHARS
        for sC in s:
            cIndex = ord(sC) - self.BASE_LOWER_CASE_UNICODE
            charMap[cIndex] += 1 

        for tC in t:
            cIndex = ord(tC) - self.BASE_LOWER_CASE_UNICODE
            charMap[cIndex] -= 1 
            if charMap[cIndex] < 0:
                return chr(cIndex + self.BASE_LOWER_CASE_UNICODE)

class SolutionThree(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # Testing case 1: "a", "ab"
        # Testing case 2: "a", "aa"  -> Missing!!!
        # Testing case 3: "abc", "bdca"
        rs = 0
        for sC in s:
            rs ^= ord(sC)
        for tC in t:
            rs ^= ord(tC)
        
        return chr(rs)

        # Similar variations
        # rs = ord(t[-1])
        # for i in xrange(len(s)):
        #     rs ^= ord(t[i])
        #     rs ^= ord(s[i])
        # return chr(rs)

# s = Solution()
# s = SolutionTwo()
s = SolutionThree()

print s.findTheDifference("a", "aa")
print s.findTheDifference("a", "ab")
print s.findTheDifference("abc", "bcda")
print s.findTheDifference("abbbbc", "abbkbbc")