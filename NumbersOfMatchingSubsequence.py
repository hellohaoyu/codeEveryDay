# Leetcode Link - https://leetcode.com/problems/number-of-matching-subsequences/description/

# Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

class Solution(object):
    def numMatchingSubseq(self, S, words):  # "abc", "a, ac, bb"
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        rs = 0
        charMap = {}
        for i in xrange(len(S)): # 0~2
            if S[i] not in charMap:
                charMap[S[i]] = [i]  # {a: [0], b:[1], c: [2]}
            else:
                charMap[S[i]].append(i)
        
        for word in words: # [a, ac, bb]
            if self.isSubseq(word, charMap):
                rs += 1
        
        return rs
    
    def isSubseq(self, word, charMap):
        curIndex = -1
        for c in word:
            if c in charMap: # 
                hasChar = False
                for i in charMap[c]:
                    if i > curIndex:
                        curIndex = i
                        hasChar = True
                        break
                if hasChar:
                    continue
            return False
            
        return True