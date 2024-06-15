#This algorithm is slow so
def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


#We will use faster technique
#in fibonacci series we find a pattern for the sum which is
# S(n) = F(n+2) - 1
#since we only need to work with last digit so, we will use pisano length i.e. 10
# and use it to lower the value with the same last digit at each nth fibonacci number

def pisano_length() : #only need a last digit so we will use pisano length as 10 as default
    previous, current = 0, 1

    for i in range(10 * 10) :
        previous, current = current, (previous + current) % 10
        if(previous == 0 and current == 1) :
            return i + 1
    return 10

def fib_sum(n) :
    #base case
    if(n <= 2) : return n

    print(pisano_length())

    n = n % pisano_length()

    print(n)
    previous, current = 0, 1

    for i in range(n+1) :
        previous, current = current, (previous + current) % 10
        
    
    return (current - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fib_sum(n))
