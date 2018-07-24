# Leetcode: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


# Key -- use the defaultdict from collections, which will reduce the code of adding val to hashMap.

from collections import defaultdict

# Clearer solution: only need to remember the number of elements left to check and also target hashMap
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        wordMap = defaultdict(int)
        for c in p:
            wordMap[c] += 1
        
        count = len(p)
        left = 0
        right = 0
        rs = []
        while right < len(s):
            wordMap[s[right]] -= 1
            if wordMap[s[right]] >= 0:
                count -= 1
            right += 1
            
            if count == 0:
                rs.append(left)
            
            if right - left >= len(p): # Please be really careful!! Add equal sign!!
                popVal = s[left]
                left += 1
                if wordMap[popVal] >= 0:
                    count += 1
                wordMap[popVal] += 1
        return rs


from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        wordMap = defaultdict(int)
        for c in p:
            wordMap[c] += 1
                
        start = len(p) - 1
        curMap = defaultdict(int)
        for c in s[:start]:
            curMap[c] += 1
            
        rs = []
        wSize = len(p)
        while start < len(s):
            curMap[s[start]] += 1  
            if self.isMapEqual(wordMap, curMap):
                rs.append(start - wSize + 1)
            popVal = s[start - wSize + 1]
            curMap[popVal] -= 1
            if curMap[popVal] == 0:
                del curMap[popVal]
            start += 1
        return rs
    
    def isMapEqual(self, m1, m2):
        for key, val in m1.iteritems():
            if key not in m2 or m1[key] != m2[key]:
                return False
        return len(m1) == len(m2)