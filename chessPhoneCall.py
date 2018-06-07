# 给一个起点，以cheese的规则拨号，看能有几种规则。

# 例子：

# 1 2 3
# 4 5 6
# 7 8 9
#   0 


# 起点： 1
# 可能的最大move：2
# 可能的拨号方式：
# 1
# 1 - 8
# 1 - 6
# 1 - 8 - 1
# 1 - 8 - 3
# 1 - 6 - 1
# 1 - 6 - 7
# 1 - 6 - 0

# 最后返回8

# def getNumOfPhoneCalls(startX, startY):


# 问了project， challenge， tight的deadline怎么prioritize task
# 1. challenge -> Testing even if it's silly simple, we still need to Testing
# 2. recommendation engine -> List, top three.
# 3. Use a time slot to focus on hard deadline.


"""
"2 * 4 - 1 / 3 * 4" = > '2 4 * 1 3 / -'
"""

# 2 4 * 1 3 / 4 * -

# ready = ture? 13/*4 /4 -
# numbers    []
# operators: [-]
#    -, +:
#    *, /:



def convertInfixToPostfix(s):
	stackOperator = []
	p = 0
	rs = ""
	while p < len(s):
		if s[p] is numbers:
			rs += s[p]
		elif s[p] in ['-', '+']:
			if not s or s[-1] in ['*', '/']:
				while stackOperator and stackOperator[]:
					rs += stackOperator.pop()
			else:
				s.append(s[p])
		elif s[p] == '(':
			s.append(s[p])
		elif 


		https://leetcode.com/problems/basic-calculator/discuss/62372/Accepted-Java-Infix-to-Postfix-based-solution-with-explaination-600ms


