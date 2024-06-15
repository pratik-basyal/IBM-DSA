#This algorithm is pretty slow so we will be using eucledian algorithma and relation between gcd and lcm

''''
def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False
'''

def gcd(a, b) :

    while(a != 0) :
        temp = a
        a = b % a
        b = temp
    return b

def lcm(a, b) :
    #relation between lcm and gcd is :
    #LCM = a * b / gcd (a, b)

    hcm = a * b #highest common multiples

    return hcm // gcd(a, b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

