# Leetcode: https://leetcode.com/problems/logger-rate-limiter/description/

# Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

# Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

# It is possible that several messages arrive roughly at the same time.

# Example:

# Logger logger = new Logger();

# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true; 

# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;

# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;

# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;

# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;

# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;



# Solution to store all the messages in history by using hashmap
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messageToTime = {}
        
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.messageToTime:
            preTime = self.messageToTime[message]
            if timestamp - preTime >= 10: # be careful about the meaning -- printed on when it's not printed in last 10 seconds
                self.messageToTime[message] = timestamp # only update the timestamp when it gets printed
                return True
            return False
            
        self.messageToTime[message] = timestamp
        return True



# Solution by only storing part of result, but it needs to use queue to check the existing message in hashMap
class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.messageToTime = {}
        
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while self.queue and (timestamp - 10 >= self.messageToTime[self.queue[0]]):  
            # Clear the item that are older than or equal to 10 seconds.
            oldMessage = self.queue.pop(0)
            del self.messageToTime[oldMessage]
        
        if message in self.messageToTime:   # After checking the time, no need to check the time. If it exists, then it means it doesn't need any things.
            return False
            
        self.messageToTime[message] = timestamp
        self.queue.append(message)
        return True