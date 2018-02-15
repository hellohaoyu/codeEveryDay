# Leetcode Link -- https://leetcode.com/problems/binary-watch/description/

# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.


# For example, the above binary watch reads "3:25".
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

# Example:
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

class SolutionOne(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        rs = []
        minsMap = self.getDigitMap(60)
        hoursMap = self.getDigitMap(12)
        
        for minOnes in xrange(num+1):
            hourOnes = num - minOnes
            # if hourOnes < 0:
            #     continue
            if minOnes in minsMap and hourOnes in hoursMap: # Easy to miss: Make sure both minOnes and hourOnes in maps.
                for minNum in minsMap[minOnes]:
                    for hourNum in hoursMap[hourOnes]:
                        minNum = '0' + str(minNum) if minNum < 10 else str(minNum)
                        hourNum = str(hourNum)
                        rs.append(hourNum + ":" + minNum)
        return rs
    def getDigitMap(self, num):
        digitMap = {}
        for i in xrange(num):
            ones = self.getOneInBin(i)
            if ones not in digitMap:
                digitMap[ones] = [i]
            else:
                digitMap[ones].append(i)
        return digitMap
   
    def getOneInBin(self, num):
        ones = 0
        while num > 0:
            if num % 2:
                ones += 1
            num = num >> 1  # Easy to miss: Update num
        return ones


class SolutionTwo(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        rs = []
        for hour in xrange(12):
            for minute in xrange(60):
                if bin(hour).count('1') + bin(minute).count('1') == num:
                    rs.append('%d:%02d' % (hour, minute))
        # Learn to use bin() and str.count()
        # Learn to use '%d:%02d' % (hour, minute)            
        
        return rs

s =  SolutionTwo()

print s.readBinaryWatch(1)
print s.readBinaryWatch(2)
