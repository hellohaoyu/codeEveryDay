# Leetcode: https://leetcode.com/problems/hand-of-straights/description/

# Alice has a hand of cards, given as an array of integers.

# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

# Return true if and only if she can.

 

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# Example 2:

# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.

class Solution(object):
    def isNStraightHand(self, hand, W):
        valToFre = {}
        for i in hand:
            if i not in valToFre:
                valToFre[i] = 1
            else:
                valToFre[i] += 1

        sortedKeys = sorted(valToFre.keys())

        for key in sortedKeys:
            if key in valToFre:
                start = key
                steps = valToFre[key] # remember to store the key value since it could be remove later.
                for i in xrange(W):
                    searchKey = start + i
                    if searchKey in valToFre:
                        valToFre[searchKey] -= steps # Remember to run steps, not 1
                        if valToFre[searchKey] < 0:
                            return False
                        if valToFre[searchKey] == 0:
                            del valToFre[searchKey]
                        continue
                    return False
        return not valToFre  # When there is no element left, it means it's complete