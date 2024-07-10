#Given coins 1 3 and 4 we need to return minimum number of coins
# Approach Dynamic Programmins
# We first find the recurrence relation and use it to solve the problem

def change(money, dp):
    # write your code here
    # m(money) = min(m(money - 1) + 1, (money - 3) + 1, (money - 4) + 1)

    #basecase
    #This approach, is lot of work and repeatitions on recursion tree
    #We can use dynamic approach as follow : 
    #Make an array to store the result for each i upto money
    if dp[money] != - 1 : return dp[money]#base case

    if money < 3 :
        dp[money] = change(money - 1, dp) + 1

    elif money >= 3 and money < 4 :
        dp[money] = min (change(money - 1, dp), change(money - 3, dp)) + 1

    elif money >= 4 :
        dp[money] = min (change(money - 1, dp), change(money - 3, dp), change(money - 4, dp)) + 1
    
    return dp[money]

if __name__ == '__main__':
    m = int(input())
    dp = [-1] * (m + 1)
    dp[0] = 0 #base case for no mo
    print(change(m, dp))
    #print(dp)
