# There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

# Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

# Initially, all the rooms start locked (except for room 0). 

# You can walk back and forth between rooms freely.

# Return true if and only if you can enter every room.

# Example 1:

# Input: [[1],[2],[3],[]]
# Output: true
# Explanation:  
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we return true.
# Example 2:

# Input: [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can't enter the room with number 2.


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        unVisited = set(range(1, len(rooms)))
        
        # Nice try to have inner function!
        def _enterRoom(i):
            unVisited.discard(i)
            for key in rooms[i]:
                if key in unVisited:
                    _enterRoom(key)
        
        _enterRoom(0)
        
        return not unVisited
        
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        unVisited = set(range(1, len(rooms)))
        keys = rooms[0]
        
        while keys and unVisited:
            l = len(keys)
            for i in xrange(l):
                key = keys.pop()
                unVisited.discard(key) # Use discard and it will not throw exception when key doesn't exist in the set.
                for newKey in rooms[key]:
                    if newKey in unVisited:
                        keys.insert(0, newKey)
        
        return not unVisited