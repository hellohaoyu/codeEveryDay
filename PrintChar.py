# print out number into Char

def numToChars(num):
	if num < 10:
		print str(num)
	chars = []
	while num > 0:
		chars.append(str(num % 10))
		num /= 10

	for i in xrange(len(chars) - 1, -1, -1):
		print chars[i]


num = 10
numToChars(num)

num = 1022304
numToChars(num)

