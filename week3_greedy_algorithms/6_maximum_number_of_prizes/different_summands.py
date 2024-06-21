
#Approach : Greedy Algorithm
'''
Greedy Choice : pick smallest number of candies possible
Sub Problem : we are left with n - smallest integer (1) at first
We won't repeat the same smallest integer and we will go with next smallest
We go until we don't cross n and for every iteration we count
We can return all smallest integers in an arrya or we can just return number of students too
'''

def optimal_summands(n):
    summands = [] #base case for 1 candy
    # write your code here
    greedy_choice = 1
    sum = 0
    while(sum + greedy_choice <= n) :
        summands.append(greedy_choice)
        sum += greedy_choice
        greedy_choice += 1

    
    if sum < n : 
        summands[- 1] += (n - sum)
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
