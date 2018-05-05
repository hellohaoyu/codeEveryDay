# In real life, service A can only be executed when service B and C have been run. Imagine there are bunch of rules like that, your input is a series of services. Please write a function to check if the service stream is valided or not.
class Service:
    def __init__(self, name):
        self.name = name 
        self.next = None

def checkIfValid(tasks, rules): # A->B->C, A:[B,C]
    preV = set()
    while tasks:
        if tasks.name in rules:
            for preReq in rules[tasks.name]:
                if preReq not in preV:
                    return False
        preV.add(tasks.name)
        tasks = tasks.next
    
    return True
    
rules1 = {'A': ['B', 'C']}
rules2 = {'B': ['A'], 'C': ['B']}


    
A = Service('A')
B = Service('B')
C = Service('C')
A.next = B
B.next = C

tasks1 = A

print checkIfValid(tasks1, rules1)
print checkIfValid(tasks1, rules2)