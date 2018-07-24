# Leetcode: https://leetcode.com/problems/group-shifted-strings/description/

# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# Example:

# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

# Key: THink of using mode to get the new value of offeset char.

class Solution(object):
    BASE_CHAR = 'a'
    BASE_CODE = ord(BASE_CHAR)
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        maps = {}
        for s in strings:
            key = self.getKey(s)
            if key in maps:
                maps[key].append(s)
            else:
                maps[key] = [s]
                
        return maps.values()
    
    def getKey(self, s):
        key = []
        curBaseCode = ord(s[0])
        for i in xrange(len(s)):
            curOffset = ord(s[i]) - curBaseCode
            newCode = self.BASE_CODE + (curOffset + 26) % 26
            key.append(chr(newCode))
        
        return "".join(key)