# -*- coding: utf-8 -*-

# 设计一个密码生成器，生成8位的，包含以下四种信息（大写字母， 小写字母， 特殊符号，数字）每个至少一个的密码。
# Follow up是如果位数也是随机的(不是8位固定)，然后信息组数也是随机的，比如不一定要每一种信息都有怎么办.

from random import randint, shuffle, choice

DIGIT_START = '0'
LOWERCASE_START = 'a'
UPPERCASE_START = 'A'
SPECIAL_CHARS = "&*%$#@!^"

def getRandomCharInRange(startChar, offset):
	return chr(ord(startChar) + randint(0, offset))

def passwordGenerator():
	rs = []

	undecided = 4
	forDigit = randint(0, undecided)
	map(lambda i: rs.append(getRandomCharInRange(DIGIT_START, 9)), range(forDigit + 1))
	
	undecided -= forDigit
	forLower = randint(0, undecided)
	map(lambda i: rs.append(getRandomCharInRange(LOWERCASE_START, 25)), range(forLower + 1))

	undecided -= forLower
	forUpper = randint(0, undecided)
	map(lambda i: rs.append(getRandomCharInRange(UPPERCASE_START, 25)), range(forUpper + 1))

	undecided -= forUpper  # All the remaining should have be special charactors!!  Be careful to miss it!!
	map(lambda i: rs.append(choice(SPECIAL_CHARS)), range(undecided + 1))

	shuffle(rs) # Shuffle is to manipulate list in place!
	return "".join(rs)

print passwordGenerator()