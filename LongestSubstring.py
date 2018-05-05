# Leetcode: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

# Longest Substring with At Most K Distinct Characters:

# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# For example, Given s = “eceba” and k = 2,

# T is "ece" which its length is 3.


# Some simple testing cases should be aware: 1. aa,1  2. ab,1  2. ab,0

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = len(s)
        if k <= 0:
            return 0
        if l <= 0 or l <= k:
            return l

        p1 = 0
        p2 = 0
        maxSize = 0
        charFreqMap = {}
        
        while p2 < l:
            curChar = s[p2]
            if curChar in charFreqMap:
                charFreqMap[curChar] += 1
                p2 += 1
                maxSize = max(maxSize, p2 - p1)
            else:
                curTypes = len(charFreqMap)
                if curTypes < k:
                    charFreqMap[curChar] = 1
                    p2 += 1
                    maxSize = max(maxSize, p2 - p1)
                    continue
                    
                while len(charFreqMap) >= k:
                    preChar = s[p1]
                    charFreqMap[preChar] -= 1
                    p1 += 1
                    if charFreqMap[preChar] == 0:
                        del charFreqMap[preChar]
                
                charFreqMap[curChar] = 1
                p2 += 1
        
        return maxSize   



# Refactored version -- 1. Use single pointer 
# Note: The max value calculation should always be added where the new char is added in the hashMap.
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = len(s)
        if k <= 0:
            return 0
        if l <= 0 or l <= k:
            return l

        p = 0
        maxSize = 0
        charFreqMap = {}
        
        for curI in xrange(l):
            curChar = s[curI]
            if curChar in charFreqMap:
                charFreqMap[curChar] += 1
                maxSize = max(maxSize, curI - p + 1)
            else:
                curTypes = len(charFreqMap)
                if curTypes < k:
                    charFreqMap[curChar] = 1
                    maxSize = max(maxSize, curI - p + 1)
                    continue
                    
                while len(charFreqMap) >= k:
                    preChar = s[p]
                    charFreqMap[preChar] -= 1
                    p += 1
                    if charFreqMap[preChar] == 0:
                        del charFreqMap[preChar]
               
                charFreqMap[curChar] = 1
        
        return maxSize   
