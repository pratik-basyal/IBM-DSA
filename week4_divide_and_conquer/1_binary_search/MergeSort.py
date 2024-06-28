#[2,4,1,5,3]

def mergesort(array) :
    #base case
    if len(array) == 1 :
        return array
    
    div = len(array) // 2
    A = mergesort(array[0:div])
    B = mergesort(array[div:len(array) + 1])

    return merge(A, B)

def merge(A, B) :
    result = [] #to store the merged array

    i = 0
    j = 0
    k = 0

    while( i < len(A) and j < len(B)) : 
        if(A[i] < B[j]) :
            result.append(A[i])
            i += 1
        
        else : 
            result.append(B[j])
            j += 1
    
    if(i < len(A)) :
        #if we still have some elements left in A to iterate
        while(i < len(A)) :
            result.append(A[i])
            i += 1

    elif(j < len(B)) :
        #if we still have some elements left in A to iterate
        while(j < len(B)) :
            result.append(B[j])
            j += 1

    return result


if __name__ == '__main__' :
    array = [12, 45, 23, 89, 56, 90, 34, 11, 78, 66]
    print(mergesort(array))