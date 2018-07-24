# -*- coding: utf-8 -*-

# Problem description: # 给若干个string, {get k combination, run，age，app, cat, dog}
# k = 3, output:[{run, age, app}, {run, age, cat}, {run, age, dog}, 
# {run, app, cat} ....]

# 1. Are the words in the list unique? Yes
# 2. Could I reuse the work in the list? No
# 3. Should I keep the relative order of words?


# {run，age，app, cat, dog} #  
#     p
#     s=0       e=l-3  (inclusive)               
# wordsToCheck =  k = 3
# single result []
# p = 0

# [run]  p = 1 []

# [2,3,1]

def getKCombinations(words, k):
	rs = []
	helper(words, 0, k, [], rs)
	return rs

def helper(words, p, k, partRs, rs):
	if k == 0:
		newRs = []
		map(lambda word: newRs.append(word), partRs)
		rs.append(newRs)
		return
	for i in xrange(p, len(words) - k + 1):
		partRs.append(words[i])
		helper(words, i + 1, k - 1, partRs, rs)
		partRs.pop()

words = [2,3,1]
k = 2
print getKCombinations(words, k)

words = ["run", "age", "app", "cat", "dog"]
k = 3
print getKCombinations(words, k)







