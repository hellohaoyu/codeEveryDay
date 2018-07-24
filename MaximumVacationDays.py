# Leetcode: https://leetcode.com/problems/maximum-vacation-days/description/

# LeetCode wants to give one of its best employees the option to travel among N cities to collect algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.

# Rules and restrictions:
# You can only travel among N cities, represented by indexes from 0 to N-1. Initially, you are in the city indexed 0 on Monday.
# The cities are connected by flights. The flights are represented as a N*N matrix (not necessary symmetrical), called flights representing the airline status from the city i to the city j. If there is no flight from the city i to the city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1. Also, flights[i][i] = 0 for all i.
# You totally have K weeks (each week has 7 days) to travel. You can only take flights at most once per day and can only take flights on each week's Monday morning. Since flight time is so short, we don't consider the impact of flight time.
# For each city, you can only have restricted vacation days in different weeks, given an N*K matrix called days representing this relationship. For the value of days[i][j], it represents the maximum days you could take vacation in the city i in the week j.
# You're given the flights matrix and days matrix, and you need to output the maximum vacation days you could take during K weeks.

# Example 1:
# Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
# Output: 12
# Explanation: 
# Ans = 6 + 3 + 3 = 12. 

# One of the best strategies is:
# 1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day. 
# (Although you start at city 0, we could also fly to and start at other cities since it is Monday.) 
# 2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
# 3rd week : stay at city 2, and play 3 days and work 4 days.

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        # DP with week and city
        numCities = len(flights)
        numWeeks = len(days[0])
        # num of days, reachable or not
        DP = [float('-inf')] * numCities 
        DP[0] = 0 # Key to init the start val to be 0!!
        
        for w in xrange(numWeeks):
            newDP = [float('-inf')] * numCities 
            for c in xrange(numCities):
                for preC in xrange(numCities):
                    if preC == c or flights[preC][c]: # Update when staying original city or flying to other cities.
                        newDP[c] = max(DP[preC] + days[c][w], newDP[c])
            DP = newDP
        return max(DP)


# More complex methods:  -> 
# If you observe, you will find the DP is get from row (N-1)th to row Nth. 
# Therefore, it's more reasonable to have one DP row and update each time! 
# (Clearer code!!)

# Please be really careful about what column means and what row means. It's easier to get confused!!
# For example, I used to believe the days[i][j] => i means city, j means week!!

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        # DP with week and city
        numCities = len(flights)
        numWeeks = len(days[0])
        # num of days, reachable or not
        DP = [[(0, False)] * numCities for _ in xrange(numWeeks)]
        
        for c in xrange(numCities):
            if c == 0 or flights[0][c]:
                DP[0][c] = (days[c][0], True)
        
        for w in xrange(1, numWeeks):
            for c in xrange(numCities):
                preVoca = 0
                isReachable = False
                for preC in xrange(numCities):
                    if (flights[preC][c] or preC == c) and DP[w-1][preC][1]:
                        preVoca = max(preVoca, DP[w-1][preC][0])
                        isReachable = True
                DP[w][c] = (0 if not isReachable else preVoca + days[c][w], isReachable)
        return max(DP[-1])[0]
