from itertools import permutations
from functools import cmp_to_key

#This is naive algorithm and is obviously slow so we need different approach
def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


#Approach : Greedy algorithm, pick up the highest number and start concatenating
'''
We need to compare two ways because of example like this : 23, 3
Suppose we have x and we take y we need to see if xy or yx is greater i.e 233 or 323 better?

We will basically use python built in insertion-sort/merge_sort to sort the numbers
We will do converting numbers into string thats the easier way to do it
We basically will need to sort it using the comparison like we discuss as a key to sort
'''

def cmp(x, y) :
    if int(x + y) > int(y + x) : 
        return -1 #x comes before y (ascending order)
    
    elif int(x+y) < int(y+x) : 
        return 1 #x comes after (means greater y)
    
    else : return 0

   
def largest_number_faster(numbers) : 
    #converting numbers into string
    num_list = list(map(str, numbers))

    #sorting the nun list
    num_list.sort(key = cmp_to_key(cmp))

    #now concatenating the elements inside num list to a string
    concate = ('').join(num_list)

    print(concate)

    #now converting into int and return the value
    return int(concate)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    #num_in_string = list(map(str, input_numbers))
    #print(num_in_string)
    print(largest_number_faster(input_numbers))
