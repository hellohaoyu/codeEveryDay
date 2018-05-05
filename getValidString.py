# Given a string, get the valid string with parentheses.
# (ab((((c)d => ab(c)d
# It could have multiple result, it's fine to return one of it.

def getValidString(s):
    leftP = [] # []
    rightP = [] # []
    deletedI = set() # O(n)
    
    for i in xrange(len(s)):  #  O(n)
        if s[i] == LEFT: # 
            leftP.append(i)  
        elif s[i] == RIGHT:
            if leftP:
                dLeft = leftP.pop()
                dRight = i
                
                deletedI.add(dLeft)
                deletedI.add(dRight)
            else:
                deletedI.add(i)
    
    for i in leftP:
        deletedI.add(i)
    
    rs = ""
    for i in in xrange(len(s)): # O(n)
        if i not in deletedI: # O(1)
            rs += s[i]
        
    return rs