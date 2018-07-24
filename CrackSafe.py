# Leetcode: https://leetcode.com/problems/cracking-the-safe/description/

# There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.

# You can keep inputting the password, the password will automatically be matched against the last n digits entered.

# For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.

# Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

# Example 1:
# Input: n = 1, k = 2
# Output: "01"
# Note: "10" will be accepted too.
# Example 2:
# Input: n = 2, k = 2
# Output: "00110"
# Note: "01100", "10011", "11001" will be accepted too.
# Note:
# n will be in the range [1, 4].
# k will be in the range [1, 10].
# k^n will be at most 4096.

# Key: assumption -- 
# 1. Reuse the last n-1 chars from last node and you are sure it will be the smallest!!
# 2. DFS and please stop earlier!! Basically, when all the nodes have reached, then it's time to stop and return the result. No global variable is needed here!


class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ["0"] * (n-1)
        visited = set()
        target = k**n
        self.DFS(ans, visited, target, n, k)
        
        return "".join(ans)
            
    def DFS(self, ans, visited, target, n, k):
        if target == len(visited):
            return True

        part = "".join(ans[-n+1:]) if n > 1 else ""  # Be careful when n == 1, it should be a empty string.
        for i in xrange(k):
            new = part + str(i)
            if new not in visited:
                visited.add(new)
                ans.append(str(i))
                if self.DFS(ans, visited, target, n, k):
                    return True
                ans.pop()
                visited.remove(new)
        return False