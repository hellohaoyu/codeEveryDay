# Merge n sorted array

import heapq

def mergeSortedArrays(arrays):
	minHeap = []
	for aI, array in enumerate(arrays):
		if array: # Mistake to use not array!!!
			minHeap.append((array[0], aI, 0))
	heapq.heapify(minHeap)

	rs = []
	while minHeap:
		cur = heapq.heappop(minHeap)
		curVal = cur[0]
		curListI = cur[1]
		curList = arrays[curListI]
		curI = cur[2]

		rs.append(curVal)
		if curI + 1 < len(curList):
			heapq.heappush(minHeap, (curList[curI + 1], curListI, curI + 1))

	return rs

arrays = [[1,2,3], [4,7,8,10], [-1, 10, 19]]

print mergeSortedArrays(arrays)
