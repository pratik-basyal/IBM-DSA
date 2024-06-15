#this naive algorithm is not worth it cause it takes lot of time
def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
 
 #The sequence of Fibonacci numbers modulo m is periodic. This repeating cycle is known as the Pisano period.
 #Since the constraint for m is <= 10^3 so we can find pisano period length for m first and then use that to reduce n
def pisano_length(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1
    return m

def fibonacci_huge_faster(n, m):
    if n <= 1:
        return n % m

    pisano_length_period = pisano_length(m)
    n = n % pisano_length_period

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_faster(n, m))
