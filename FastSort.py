# [4,2,3,1]

# [1,2,3,4]


# [3, 1, 2, 5, 4]
#    p1        p2

# [3, 1, 2, 5, 4]
#       p1p2

# [2, 1, 3, 5, 4]
#      p1 p2


# Sort[2, 1], Sort[5, 4]
#       [3]
#

# Time complexity: O(nlogn), Space complexity: O(1)

def fastSort(nums):
	help(0, len(nums) - 1, nums)

def help(s, e, nums):
	if s >= e:
		return

	pivotal = nums[s]
	p1 = s    
	p2 = e    
	while p1 < p2: 
		if nums[p2] > pivotal: # p2 goes first!!! VERY VERY IMPORTANT! (Starting from right to left first)
			p2 -= 1
			continue
		if nums[p1] <= pivotal:
			p1 += 1
			continue

		temp = nums[p1]  # (we could check if p1 == p2, then we could choose not to swap!!)
		nums[p1] = nums[p2]
		nums[p2] = temp

	temp = nums[s] 
	nums[s] = nums[p2]
	nums[p2] = temp

	help(s, p1-1, nums)  # Sort left part
	help(p2+1, e, nums)  # Sort right part

a = [3,1,2]
# a = [3,1]
a = [3,1,2,4,1,1,2,-1]
# a = [3,1]
fastSort(a)
print a


# We should be really careful about p2 should go firstly!!!


# What's the worse case for quick sort?
# Example: [10,9,8,7,6,5]






