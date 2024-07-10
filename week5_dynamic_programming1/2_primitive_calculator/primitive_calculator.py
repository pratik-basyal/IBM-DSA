'''
Every time we multiply by 3 for one means, we divide by 3
'''
import math

def compute_min_operations(n, dp):
    # +1, *2, *3
    #[1,2,3,4,5,6,7,8,9,10,11]
    #[0,1,1,2]
    #base case for recursion relation :

    '''
    if dp[n] != math.inf : return dp[n]
    this recursion process can not extend 10 ^ 3 so I will just comment it out and use iteration process instead
    dp[n] = min(compute_min_operations(n - 1, dp) + 1, compute_min_operations(n//2, dp) + 1 if n % 2 == 0 else dp[n], 
                compute_min_operations(n // 3, dp) +1 if (n % 3 == 0) else dp[n])
    '''
    if n <= 1 : return [0]

    else :
        i = 2
        while i <= n :
            dp[i] = min (dp[i - 1] + 1, dp[i // 2] + 1 if i % 2 == 0 else dp[i], dp[i // 3] + 1 if i % 3 == 0 else dp[i])
            i += 1

    return dp


if __name__ == '__main__':
    input_n = int(input())
    #Will use 1D dp array to store the result for each n upto n + 1 index
    #for the base case we have dp[0] and dp[1] = 0

    dp = [math.inf] * (input_n + 1)
    dp[0] = 0 #base case for dp
    dp[1] = 0

    n = input_n

    compute_min_operations(n, dp)

    output_sequence = []
    output_sequence.append(n)

    #we can back track from our dp table to fill the output sequence and heres how :
    while (n > 1) :
        if dp[n] == dp[n -1] + 1 :
            #print("TRUE,  because : dp[n] = ", dp[n], "and dp[n-1] = ", dp[n - 1], "and n = ", n)
            n = n - 1
            output_sequence.insert(0, n)
        
        elif n % 2 == 0 and dp[n] == dp[n // 2] + 1 :
            #print("TRUE,  because : dp[n] = ", dp[n], "and dp[n // 2] = ", dp[n // 2], "and n = ", n)
            n = n // 2
            output_sequence.insert(0, n)
        
        elif n % 3 == 0 and dp[n] == dp[n // 3] + 1 :
            #print("TRUE,  because : dp[n] = ", dp[n], "and dp[n-1] = ", dp[n // 3], "and n = ", n)
            n = n // 3
            output_sequence.insert(0, n)
        
        else :
            break
    print(len(output_sequence) - 1)
    print(*output_sequence)
    #print(dp)
    #print(dp)
    #1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
    #“1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117 96234”.