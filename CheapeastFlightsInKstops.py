# Leetcode: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

# There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

# Now given all the cities and fights, together with starting city src and the destination dst, your task is 
# to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

import heapq
from collections import defaultdict
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        flightsMap = defaultdict(dict) # Default dict with dict -- Good usage!
        for f, t, p in flights:
            flightsMap[f][t] = p
            
        heap = [(0, src, K+1)] # (price, cur, flightsLeft) -> Smart with tuple!, use heap to pop the smallest price!
        while heap:
            price, src, flightsLeft = heapq.heappop(heap)
            if src == dst:
                return price
            if flightsLeft > 0:
                for nextC in flightsMap[src]:
                    heapq.heappush(heap, (price + flightsMap[src][nextC], nextC, flightsLeft-1))
        return -1