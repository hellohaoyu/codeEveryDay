def bucketSort(nums, maxNum):
	buckets = [0] * (maxNum + 1)

	for i in nums:
		buckets[i] += 1


	for v in xrange(maxNum + 1):
		times = buckets[v]
		for i in xrange(times):
			print v


bucketSort([5,4,1,4,2,1], 5)

# Weakness: Need a lot of extra memory if the list contains large number
# Weakness: If there is float number, it can't be handled normally

# Time complexity: O(M+N), m is the number of bukets, n is the number of numbers to sort.
# Space complexity: O(M)