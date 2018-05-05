def bubbuleSort(nums):
	t  = len(nums) - 1
	while t >= 1:
	# for t in xrange(1, len(nums)) # [1, 2]
		for i in xrange(t): # 1 -> [0], 2 -> [0, 1]
			if nums[i] > nums[i + 1]: # [0] [1]
				temp =  nums[i]
				nums[i] = nums[i+1]
				nums[i+1] = temp
		t -= 1

a = [1, 0, 2, 10, -9, 4]
bubbuleSort(a)
print a

# Time complexity: O(n^2) , Space complexity: O(1)

