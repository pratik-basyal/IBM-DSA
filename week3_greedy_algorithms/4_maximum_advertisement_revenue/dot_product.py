from itertools import permutations


#This solution is taking every permutations possible
#This makes it slow as fuck
#We need to come up with some better idea
def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product

#Approach : 
'''
I think, we can simply sort the prices and click and just multiply using greedy approach
Once we sort, we will have option to choose greatest one every time and multyply it to find the max product
'''

def max_dot_product_faster(prices, clicks) : 
    prices.sort(reverse = True)
    clicks.sort(reverse = True)

    max_product = 0

    for i in range(len(prices)) :
        max_product += prices[i] * clicks[i]

    return max_product

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product_faster(prices, clicks))
    
