#Example
'''
Port
Sorts
'''

def edit_distance(first_string, second_string):
    #Approach :
    '''
    Recurrence relation : 
    ED(i,j) = min(ED(i-1, j) + 1, ED(i, j-1) + 1, if A(i) = B(j) ED(i-1, j-1), else 1 + ED(i - 1, j - 1))
    '''
    i = len(first_string) - 1 #pointer to the index of first string
    j = len(second_string) - 1 # pointer to the index of second string
    
    #Base case
    if(len(first_string) == 0) : return len(second_string)

    elif (len(second_string) == 0) : return len (first_string)

    dp = [[0] * (len(second_string) + 1) for _ in range(len(first_string) + 1)] #storing result in 2D array

    #Recursion relation
    '''
    #This recursion relation gives 2 ^ (n/2) time complexity which is really bad so we will be using dynamic programming with same recursion relation
    return min(1 + edit_distance(first_string[:i], second_string[:j+1]), edit_distance(first_string[:i+1], second_string[:j]) + 1, 
               edit_distance(first_string[:i], second_string[:j]) 
               if first_string[i] == second_string[j] else edit_distance(first_string[:i], second_string[:j]) + 1)
    '''
    for i in range(len(first_string) + 1) :
        for j in range(len(second_string) + 1) :
            if i == 0 : #base case
                dp[i][j] = j
                
            elif j == 0:
                dp[i][j] = i
                
            else :
                dp[i][j] = min (dp[i-1][j-1] if first_string[i - 1] == second_string[j - 1] else dp[i-1] [j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
        
    return dp[len(first_string)][len(second_string)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
