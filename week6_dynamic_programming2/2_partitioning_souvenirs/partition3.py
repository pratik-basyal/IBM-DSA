from sys import stdin

def partition3(values):
    total_sum = sum(values)
    n = len(values)
    
    # If the total sum is not divisible by 3, we cannot partition into three equal subsets
    if total_sum % 3 != 0:
        return 0
    
    subset_sum = total_sum // 3
    
    # Dynamic programming approach
    dp = [[[False] * (subset_sum + 1) for _ in range(subset_sum + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True
    
    for i in range(1, n + 1):
        for j in range(subset_sum + 1):
            for k in range(subset_sum + 1):
                dp[i][j][k] = dp[i-1][j][k]
                if j >= values[i-1]:
                    dp[i][j][k] = dp[i][j][k] or dp[i-1][j - values[i-1]][k]
                if k >= values[i-1]:
                    dp[i][j][k] = dp[i][j][k] or dp[i-1][j][k - values[i-1]]
    
    return 1 if dp[n][subset_sum][subset_sum] else 0

if __name__ == '__main__':
    input_n = int(input())

    data = stdin.readline().strip().split()
    input_values = list(map(int, data))
    assert input_n == len(input_values)
    print(partition3(input_values))
