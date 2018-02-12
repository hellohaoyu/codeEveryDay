# https://leetcode.com/problems/add-two-numbers/description/

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Testing Cases:
# [2,4,3]
# [5,6,4]  => [7, 0 , 8]

# [0], [0] => [0]

# [0], [0, 1] => [0, 1]

# [9], [9] => [8, 1]

# [1], [9,9,9] -> [0,0,0,1]

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        inc = 0
        cur1 = l1 
        cur2 = l2
        rs = ListNode(0)
        curRs = rs
        while cur1 and cur2:
            curVal = cur1.val + cur2.val + inc=
            if curVal >= 10:
                curVal %= 10
                inc = 1  
            else:
                inc = 0
            newNode = ListNode(curVal)
            curRs.next = newNode
            curRs = newNode
            cur1 = cur1.next 
            cur2 = cur2.next
        
        if inc == 0:
            if cur1:
                curRs.next = cur1
            elif cur2:
                curRs.next = cur2
        else:
            if cur1:
                self.addRestOfList(cur1, inc, curRs)
            elif cur2:
                self.addRestOfList(cur2, inc, curRs)
            else:
                curRs.next = ListNode(1)
        
        return rs.next
    
    def addRestOfList(self, l, inc, curRs):
        while l:
            curVal = l.val + inc
            if curVal >= 10:
                curVal %= 10
                inc = 1   
            else:
                inc = 0
            newNode = ListNode(curVal)
            curRs.next = newNode 
            curRs = newNode
            l = l.next
        
        if inc == 1:
            curRs.next = ListNode(1)
