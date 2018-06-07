# Leetcode: https://leetcode.com/problems/bold-words-in-string/description/

# Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

# The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

# For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

# Note:

# words has length in range [0, 50].
# words[i] has length in range [1, 10].
# S has length in range [0, 500].
# All characters in words[i] and S are lowercase letters.


# Very easy to make mistake!!

class Solution(object):
    def boldWords(self, words, S): # [bb], abba, 
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        l = len(S)
        tags = [False] * l
        
        for word in words:
            sI = 0
            lw = len(word)
            while sI < l and S.find(word, sI) >= 0:
                wordSI = S.find(word, sI)
                for i in xrange(lw):
                    tags[wordSI + i] = True 
                sI += 1 # Remember to plus one by one becase the case of overlapping!
        
        sI = 0
        rs = [] # a, 
        while sI < l:
            if not tags[sI]:
                rs.append(S[sI])
                sI += 1
                continue
            eI = sI
            while eI < l and tags[eI]: # Remember to add boundary checking when acessing list.
                eI += 1
            rs.append('<b>' + S[sI:eI] + '</b>')
            sI = eI
        
        return "".join(rs) 