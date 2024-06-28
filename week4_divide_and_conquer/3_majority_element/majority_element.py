#This technique has quadratic time complexity O(n^2)
def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

#Approach : Linear approach
'''
We can't use count array cause the constraints is too high
We can use dictionary with key as element and value as its frequency
'''

def majority_element_faster(elements) : 
    dictionary = {} #key as element and frequency as value
    
    length = len(elements)
    for e in elements :
        if(e in dictionary) :
            dictionary[e] = dictionary[e] + 1
            if (dictionary[e] > length / 2) : return 1

        else : 
            dictionary[e] = 1
    
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_faster(input_elements))
