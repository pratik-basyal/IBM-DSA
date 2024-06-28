from random import randint


def partition3(array, left, right):
    # write your code here
    m1, m2 = left, left

    pivot = array[left] #pivot element

    for i in range(left + 1, right + 1) : 
        current = array[i]
        if(current > pivot) : continue

        elif (current == pivot) : 
            temp = current
            del(array[i])
            array.insert(m1, temp)
            m2 += 1
        
        else :
            temp = current
            del(array[i])
            array.insert(m1, temp)
            m1 += 1
            m2 += 1
    
    return (m1, m2)


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    #print(k)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)

    print("k : ", k, "m1 :", m1, "m2 : ", m2)

    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
