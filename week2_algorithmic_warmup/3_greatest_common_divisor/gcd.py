import random

#this algorithm will be slow so we will ignore this one
'''
def gcd(a, b):
    current_gcd = 1
    testor = 2
    #using school level idea to implement HCF
    while (True) :
        if(testor > min(a,b)) : break

        if (a % testor == 0) &  (b % testor == 0):
            a = a // testor
            b = b // testor
            current_gcd *= testor
            testor = 2
        
        else :
            testor += 1

    return current_gcd
'''

def gcd(a,b) :
    #using Euclidean algorithm
    #This is based on principle that, gcd also divides the difference of that number

    #just divide a and b until the remainder is 0
    while(a != 0) :
        store = a
        a = b % a
        b = store

    return b

#testing randomly
'''
def test() :
    first = random.randint(2, 10000)
    second = random.randint(2, 10000)
    print("first : ", first, "second : ", second)
    print(gcd(first, second))
'''

if __name__ == "__main__":
    
    a, b = map(int, input().split())
    print(gcd(a, b))
