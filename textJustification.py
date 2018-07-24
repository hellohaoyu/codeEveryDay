# Leetcode: https://leetcode.com/problems/text-justification/description/

# Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
# Example 1:

# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be",
#              because the last line must be left-justified instead of fully-justified.
#              Note that the second line is also left-justified becase it contains only one word.
# Example 3:

# Input:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]


# 1. 
# 

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        rs = []
        curI = 0
        while curI < len(words):
            newCurI = self.getWordsForSingleLine(curI, words, maxWidth)
            rs.append(self.createNewLine(curI, newCurI, words, maxWidth))
            curI = newCurI
        
        return rs
    
    def createNewLine(self, sI, eI, words, maxWidth):
        rs = []
        gaps = eI - sI - 1
        isLeftJustify = gaps == 0 or eI == len(words)
        if isLeftJustify:
            wordsWithspaces = " ".join(words[sI:eI])
            return wordsWithspaces + " " * (maxWidth - len(wordsWithspaces))

        availableSpaces = maxWidth
        for i in xrange(sI, eI):
            availableSpaces -= len(words[i])
        
        baseNumSpaces = (availableSpaces / gaps)
        numSpaces = [baseNumSpaces] * gaps
        extraSpaces = availableSpaces % gaps
        for i in xrange(extraSpaces):
            numSpaces[i] += 1
        
        rs = []
        for i in xrange(gaps):
            rs.append(words[sI + i]) # relative position!! Bug found!!
            rs.append(" " * numSpaces[i])
        rs.append(words[eI - 1])
        return "".join(rs)
        
    
    def getWordsForSingleLine(self, curI, words, maxWidth):
        availableSpaces = maxWidth
        while curI < len(words) and availableSpaces >= len(words[curI]):
            availableSpaces -= len(words[curI]) + 1
            curI += 1
        return curI


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        rs = []
        cur = []
        numOfLetters = 0 
        for w in words:
            if numOfLetters + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    rs.append("".join(cur) + " " * (maxWidth - len(cur[0]))) #
                else:
                    for i in xrange(maxWidth - numOfLetters):
                        cur[i % (len(cur) - 1 or 1)] += " "  # remember to check len(cur) - 1 mean to add space to the words whose index is from 0 ~ len(word) - 2
                    rs.append("".join(cur))
                # Reset values
                numOfLetters = 0
                cur = []
                
            cur += [w]
            numOfLetters += len(w)
        
        return rs + [" ".join(cur).ljust(maxWidth)]