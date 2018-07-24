# Leetcode: https://leetcode.com/problems/word-break-ii/description/

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:

# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {}) # leetcode, leet code, 
    
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        rs = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if s == word:
                rs.append(word)  # Remember single word as a result is just one type of rs and couldn't just return all!!
            else:
                for preS in self.helper(s[len(word):], wordDict, memo):
                    rs.append(word + " " + preS)
                
        memo[s] = rs
        return rs


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # Check if it's breakable or not!! Otherwise, it will keep going!
        DP = [False] * (len(s) + 1)
        DP[0] = True
        
        for i in xrange(len(s)):
            for j in xrange(i+1, len(s) + 1):
                if DP[i] and s[i:j] in wordDict:
                    DP[j] = True
        
        if not DP[-1]:
            return []
    
    
        # After checking to gurantee to have results, then apply the BP algorithm again!
        DP = [False] * (len(s) + 1)
        DP[0] = True
        vals = [ [] for i in xrange(len(s) + 1) ]
        hashMap = {}
        
        for sI in xrange(len(s)):
            for eI in xrange(sI+1, len(s) + 1):
                if DP[sI] and s[sI:eI] in wordDict:
                    DP[eI] = True
                    newWord = s[sI:eI]
                    if vals[sI]: # not empty
                        for words in vals[sI]:
                            newWords = []
                            map(lambda w : newWords.append(w), words)
                            newWords.append(newWord)
                            vals[eI].append(newWords)
                    else:
                        vals[eI].append([newWord])
        rs = []    
        map(lambda words: rs.append(" ".join(words)), vals[len(s)])
        return rs