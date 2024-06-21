from sys import stdin


#Approach : Greedy approach
'''
We are going to use greedy approach
First choice max value i.e. max(value/weight)
After that we can put as much weights as we can from this item
If knapsack is not full then we can move on and repeat the process

To find the max value we need to go through n operation each time so timecomplexity would be O(n^2)
To reduce thsi time complexity we will sort this according to value per each weight
'''

def optimal_value(capacity, weights, values):
    #lets create an array that stores value / weight
    unit_value = []
    for i in range(len(weights)) :
        unit_value.append((values[i] / weights[i], i))
    
    unit_value.sort(reverse = True) #sorting in descending order

    value = 0
    # write your code here
    for unit in unit_value :
        if(capacity == 0) : return value
        w = weights[unit[1]]
        a = min(capacity, w)
        value += unit[0] * a
        capacity = capacity - a
    return value


if __name__ == "__main__":

    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    
