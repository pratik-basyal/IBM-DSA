# Uses python3
import sys

#this algorithm is like a brute force and is pretty slow
'''
def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10
'''

#using some technique that doesn't take too much of a time
#what we can do is we can prolly find the sum S(n) and S(m)
#subtract the difference of S(n) and S(m)

#this function will basically return the length of sequence of F(n) module 10 until it repeats
def pisano_length() :
    current = 1
    previous = 0
    for i in range(0, 10 * 10) :
        previous, current = current, (previous + current) % 10
        if(previous == 0 and current == 1) :
            return i + 1
    return 60

'''
def fib_partial_sum_faster(m, n) :
    m = m % picano_length() #reducing length of m
    n = n % picano_length() #reducing length of n

    previous = 0
    current = 1

    sum_m = 0
    sum_n = 0

    for i in range(n+1) :
        previous, current = current, (current + previous) % 10
        if(i == m) : sum_m = previous - 1
        sum_n = current - 1
    
    #now difference of sum m and n
    return (sum_n - sum_m) % 10
'''

def fibonacci_modulo(n, m):
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def fib_partial_sum_faster(m, n):
    # Get Pisano period length for modulus 10
    pisano_period_length = pisano_length()

    # Reduce m and n using Pisano period length
    m = m % pisano_period_length
    n = n % pisano_period_length

    if n < m:
        n += pisano_period_length

    # Compute F_{m+1} and F_{n+2} modulo 10
    F_m_plus_1 = fibonacci_modulo(m + 1, 10)
    F_n_plus_2 = fibonacci_modulo(n + 2, 10)

    # Calculate the sum modulo 10
    sum_n = (F_n_plus_2 - 1) % 10
    sum_m_minus_1 = (F_m_plus_1 - 1) % 10

    # Calculate the partial sum modulo 10
    partial_sum = (sum_n - sum_m_minus_1 + 10) % 10

    return partial_sum

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fib_partial_sum_faster(from_, to))
