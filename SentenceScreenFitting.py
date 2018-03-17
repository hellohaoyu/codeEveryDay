# Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.

# Note:

# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
 

# Example 1:

# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]

# Output: 
# 1

# Explanation:
# hello---
# world---


# Time exceed limit error - But logic should be fine.
# Still easy to make mistakes:
# remember to test those testing cases:
#    1 row, 10 cols, ["Hello", "me"] / ["Hello", "meme"]
#    2 row, 6 cols,  [ "Hellooo"]
class Solution(object):
    def wordsTyping(self, sentence, rows, cols): # [a,a], 2, 2
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        rs = 0
        curRow = 1
        curCol = 0
        p = 0
        ls = len(sentence)
        wordLens = []
        for word in sentence:
            wordLens.append(len(word))
            
        while curRow <= rows:
            newCurCol = curCol + wordLens[p]
            if newCurCol == cols:  # Fit in last part and go to next line
                curRow += 1
                curCol = 0
                p += 1
            elif newCurCol < cols:  # Fit in without full
                curCol = newCurCol + 1
                p += 1
            else:                   # Can't fit in and go to next line
                curRow += 1
                curCol = 0
            
            if p == ls:
                if curRow <= rows:
                    rs += 1
                    p = 0
        
        if curCol == 0 and p == ls:
            rs += 1
        return rs