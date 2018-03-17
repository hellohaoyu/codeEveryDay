# Leetcode: https://leetcode.com/problems/min-stack/description/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.



# Best solution -- only use one stack
# the values in the stack are the difference between previous min or current min. 
# Only need a variable to store the min.
import sys
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxint
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            newVal = x - self.min
            self.stack.append(newVal)
            if newVal < 0:
                self.min = x
        else:
            self.stack.append(0)
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            if self.stack[-1] < 0:
                self.min = self.min - self.stack[-1]
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            if self.stack[-1] >=0:
                return self.min + self.stack[-1]
            return self.min
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.min



# Method 2 by using two stacks
# use one stack to store min values and another to act as normal stack list.
# remember to deal with the case when there are multipe min values (Solution: need to store duplicates in min value list)
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVals = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.minVals:
            if self.minVals[-1] >= x:
                self.minVals.append(x)
        else:
            self.minVals.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            val = self.stack.pop()
            if val == self.getMin():
                self.minVals.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.minVals:
            return self.minVals[-1]