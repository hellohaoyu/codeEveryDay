# Use stack to check palindrome

def checkPalindrome(s):
	l = len(s)
	mid = l/2

	stack = []
	for i in xrange(mid): 
		stack.append(s[i])

	if l % 2:
		mid += 1
	for i in xrange(mid, l):  
		v = stack.pop()
		if v != s[i]:
			return False

	return True

a = [1, 2, 1]
print checkPalindrome(a)

b = [2, 1, 1, 2]
print checkPalindrome(b)

c = [4,3,3,5]
print checkPalindrome(c)

# Storage ->  O(n/2)

