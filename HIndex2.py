# Leetcode: https://leetcode.com/problems/h-index/description/

# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

# Note: If there are several possible values for h, the maximum one is taken as the h-index.

# FollowUp: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

# [0, 1]

# bucket solution:


# Sorted and non-binary search solution
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        # 0, 0, 1]
        rs = 0
        l = len(citations)
        
        rs = 0
        while rs < l and citations[l - rs - 1] > rs:  # 5 - 0 - 1 = 4 => 2 > 2
            rs += 1
        
        return rs


# FollowUp solution:
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        s = 0
        l = len(citations)
        e = l - 1 
        
        while s <= e: 
            mid = (s + e) / 2
            if citations[l - mid - 1] < mid:
                e = mid -1
            elif citations[l - mid - 1] > mid:
                s = mid +1 # e=0
            else:    
                return mid
        
        return s