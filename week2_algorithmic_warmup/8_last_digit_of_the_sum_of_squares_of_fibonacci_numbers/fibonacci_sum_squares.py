#this algortihm is slow
'''
def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
'''

#we have this direct formula after finding the pattern
#S(n^2) = [{F(n) % 10} * {F(n+1) % 10}]
#to find the last digit we find the modulo of that

#since we know the pisano length of modulo 10 already I won't be using function to calculate it
def fibonacci_sum_squares_faster(n) : 
    #first reducing the nth number
    n = n % 60
    sum = 0

    previous, current = 0, 1
    for i in range(0, n) :
        previous, current = current, (previous + current) % 10
        sum = previous * current

    return sum % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_faster(n))
