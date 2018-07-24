class Calendar(object):
    MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP_FEB_MONTH = 29
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getNewDate(self, offset):
        newCalendar = Calendar(self.year, self.month, self.day)
        # No year change
        if offset <= self.getRestDaysInFollowingMonthes():
            self.setNewMonthAndDay(newCalendar, offset)
            return newCalendar

        # Has year change
        newYear = self.year + 1
        offset -= self.getRestDaysInFollowingMonthes()
        while offset > self.getDaysInYear(newYear):
            offset -= self.getDaysInYear(newYear)
            newYear += 1

        offset -= 1
        newCalendar = Calendar(newYear, 1, 1)
        return newCalendar.getNewDate(offset)

    def __str__(self):
        return "year: " + str(self.year) + ", month: " + str(self.month) + ", day:" + str(self.day)


    def getRestDaysInCurMonth(self):
        if self.isLeapYear(self.year) and self.month == 2:
            return self.LEAP_FEB_MONTH - self.day

        return self.MONTH_DAYS[self.month - 1] - self.day

    def setNewMonthAndDay(self, calendar, offset):
        restDaysInCurMonth = calendar.getRestDaysInCurMonth()
        if offset <= restDaysInCurMonth:
            calendar.day += offset
            return

        curMonth = calendar.month + 1
        curOffset = offset - restDaysInCurMonth

        while curOffset > self.MONTH_DAYS[curMonth - 1]:
            curOffset -= self.MONTH_DAYS[curMonth - 1]
            curMonth += 1

        calendar.month = curMonth
        calendar.day = curOffset

    def getRestDaysInFollowingMonthes(self):
        restDays = sum(self.MONTH_DAYS[self.month:]) + self.getRestDaysInCurMonth()
        if self.isLeapYear(self.year) and self.month == 1:
            restDays += 1

        return restDays

    def getDaysInYear(self, year):
        return 366 if self.isLeapYear(year) else 365

    def isLeapYear(self, year):
        return year % 4 == 0


c = Calendar(2018, 2, 3)
print c.getNewDate(7)

c = Calendar(2018, 2, 19)
print c.getNewDate(20)

c = Calendar(2018, 12, 30)
print c.getNewDate(2)

c = Calendar(2018, 12, 30)
print c.getNewDate(1000)
        