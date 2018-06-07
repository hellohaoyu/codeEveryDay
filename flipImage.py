# Leetcode: https://leetcode.com/problems/flipping-an-image/description/

# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Example 1:

# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:

# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

# Be careful about the invert of the middle index,


def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    if not A or not A[0]:
        return A
    numRows = len(A) # 1
    numCols = len(A[0]) # 3
    for r in xrange(numRows):
        s = 0
        e = numCols - 1
        while s <= e:
            temp = (A[r][s] ^ 1)
            A[r][s] = (A[r][e] ^ 1)
            A[r][e] = temp
            s += 1
            e -= 1
    return A

inputV = [[1,1,0]]

print flipAndInvertImage(inputV)