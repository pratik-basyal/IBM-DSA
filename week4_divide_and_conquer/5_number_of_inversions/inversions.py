from itertools import combinations

inversion = 0

#this is just slow and naive algorithm
def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


#Approach : we will use merge sort(divide and conquer) technique
'''
We can count the inversion at the same time of merging/conquering
We divide an array into 1/2 everytime and we can sort and count the inversion at the same time
'''

def inversion_faster(a) : 

    #base case for recursion
    if len(a) == 1 : return a

    #mid = left + (right - left) // 2 #divided array into 2 half
    mid = len(a) // 2

    left_array = inversion_faster(a[0 : mid])
    right_array = inversion_faster(a[mid : len(a)])

    return count_inversion(left_array, right_array)

def count_inversion(left_array, right_array) :
    global inversion

    result = []
    i = 0 #pointer to left array
    j = 0 #pointer to right array


    while(i < len(left_array) and j < len(right_array)) :

        if(left_array[i] > right_array[j]) :
            result.append(right_array[j])
            j += 1
            inversion += len(left_array) - i

        elif(left_array[i] <= right_array[j]) :
            result.append(left_array[i])
            i += 1
    
    # if theres still element to be left to traverse on left array
    result.extend(left_array[i:])
    
    # if theres still element to be left to traverse on right array
    result.extend(right_array[j:])

    #print("Left array : ", left_array, "Right array :", right_array, "Inversion : ", inversion)


    return result

if __name__ == '__main__':

    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    inversion_faster(elements)
    print(inversion)
