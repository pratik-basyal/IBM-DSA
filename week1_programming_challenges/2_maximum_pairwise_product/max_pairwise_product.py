import random

'''
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
'''



#mycode = max_pairwise_product_faster([1,2,3,4])

#defined = max_pairwise_product([1,2,3,4])

#will generate a stress tests on main method and use it to run the program




if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))

    '''
    while(True) :
        rand_n = random.randint(1,20)

        numbers = []
        for i in range(0, rand_n) : 
            numbers.append(random.randint(1,1000))
        
        if(max_pairwise_product(numbers) != max_pairwise_product_faster(numbers)) :
            print(numbers)
            print("defined result : ", max_pairwise_product(numbers), "\nmy result : ", max_pairwise_product_faster(numbers))
            break
        
        else :
            print("OK")
    '''