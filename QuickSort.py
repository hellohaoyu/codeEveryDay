# Quick sort

# [1,3,4,2,6]
#    p1    p2

# [1,3,4,2,6]

# [1, 3,4,2,6]
  
# Left: []

# mid: 1

# Right: [3, 4, 2, 6] 
          #      p2
          #    p1
          # 3    
            
          #   p1 < p2      
def quickSort(nums): # [2, 1, 3]
	helper(nums, 0, len(nums)) # 0 ~ 3

def helper(nums, s, e):
	if e - s <= 1: # 3 - 0
		return 
	p = s  # 0 => 2
	p1 = s # 0 => 1
	p2 = e - 1 # 1 => 1

	while p1 < p2: # 1 < 1
		if nums[p2] > nums[p]: 
			p2 -= 1
			continue
		if nums[p1] <= nums[p]:
			p1 += 1
			continue
		nums[p1], nums[p2] = nums[p2], nums[p1]
		p1 += 1
		p2 -= 1

	nums[p2], nums[p] = nums[p], nums[p2]
	helper(nums, s, p2)
	helper(nums, p2+1, e)


# nums = [2, 1, 3]
# quickSort(nums)


nums = [7, 3, 10, 2, 1, 3, 11]
       mid
        pL              
                        pR   

      

      [3, 2, 1, 3,     7, 10,11]
           

     [left          ] 7 [right]
   


print nums
quickSort(nums)
print nums


