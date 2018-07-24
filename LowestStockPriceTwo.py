import heapq

class Price(object):
	"""docstring for Price"""
	def __init__(self, startTime, endTime, price):
		super(Price, self).__init__()
		self.startTime = startTime
		self.endTime = endTime
		self.price = price

class EndTimeAndPrice(object):
     	"""docstring for EndTimeAndPrice"""
     	def __init__(self, price, endTime):
     		self.endTime = endTime
     		self.price = price
     	def __cmp__(self, other):
			if self.price < other.price:
				return -1
			elif self.price > other.price:
				return 1
			else:
				return 0
def getLowestPriceRange(prices):
	rs = []
	if not prices:
		return rs

	prices.sort(key = lambda price : -price.startTime) # Descending order by start time

	endPrices = []
	heapq.heapify(endPrices) # sorted by price

	curStockPrice = prices.pop()
	heapq.heappush(endPrices, EndTimeAndPrice(curStockPrice.price, curStockPrice.endTime))
	startTime = curStockPrice.startTime
	bestPrice = curStockPrice.price

	while prices:
		curStockPrice = prices.pop()
		newStartTime = curStockPrice.startTime

		# Clear all the expired slots
		while endPrices and endPrices[0].endTime < startTime:
			heapq.heappop(endPrices)

		if not endPrices:
			break;

		bestPrice, bestPriceEndTime = endPrices[0].price, endPrices[0].endTime
		if bestPriceEndTime >= newStartTime:
			rs.append(Price(startTime, newStartTime, bestPrice))
			startTime = newStartTime
		else:
			rs.append(Price(startTime, bestPriceEndTime, bestPrice))
			startTime = bestPriceEndTime

		heapq.heappush(endPrices, EndTimeAndPrice(curStockPrice.price, curStockPrice.endTime))

	# Clear all the expired slots
	while endPrices:
		endPrice = heapq.heappop(endPrices)
		if endPrice.endTime > startTime:
			rs.append(Price(startTime, endPrice.endTime, endPrice.price))
			startTime = endPrice.endTime

	mergedRs = []
	pre = rs[0]
	for p in rs[1:]:
		if pre.endTime == p.startTime and pre.price == p.price:
			pre = Price(pre.startTime, p.endTime, p.price)
		else:
			mergedRs.append(pre)
			pre = p

	mergedRs.append(pre)

	return mergedRs

def printPriceList(prices):
	for p in prices:
		print "startTime: " + str(p.startTime) + ", endTime: " + str(p.endTime) + ", price: " + str(p.price)

prices = [Price(1, 3, 2), Price(2, 5, 4), Price(4, 5, 1)]
printPriceList(getLowestPriceRange(prices))
# Expected:
# startTime: 1, endTime: 2, price: 2
# startTime: 2, endTime: 4, price: 4
# startTime: 4, endTime: 5, price: 1


# prices = [Price(1, 10, 2), Price(2, 6, 5), Price(3, 7, 6), Price(6, 8, 7), Price(6, 9, 4)]
# printPriceList(getLowestPriceRange(prices))
# startTime: 1, endTime: 10, price: 2

# prices = [Price(1, 10, 2), Price(2, 6, 5)]
# printPriceList(getLowestPriceRange(prices))

