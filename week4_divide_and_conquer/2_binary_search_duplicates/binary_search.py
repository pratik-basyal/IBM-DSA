def binary_search(keys, query):
    # write your code here
    #since keys are sorted
    left = 0
    right = len(keys) - 1
    result = -1 #default value if we don't find the query

    while(left <= right) :
        middle = left + (right - left) // 2
        #for duplicates element : even after we find the element we continue searching for the query
        if keys[middle] == query :
            result = middle
            right = middle - 1

        elif keys[middle] < query :
            left = middle + 1
        
        elif keys[middle] > query :
            right = middle - 1
    

    return result

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
