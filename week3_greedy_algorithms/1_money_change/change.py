
#Approach : 
'''
i. Greedy Approach strategy : 
ii. Greedy choice, proving it safe and repeat for sub-problems
iii. With the greedy approach, we pick the highest denomination that doesn't exceed money
iv. And we will prove it that it will get us to the optimal soln:
v. Proof by induction :
    IH : For any value of k < n, it will have an optimal solution
    there will be 3 cases :
    if c = 10, problem reduces to n-10, and by IH it holds true for n - 10 value
    if c = 5, means n > 5 and n < 10, so now for n-5 IH holds true too
    if c = 1, then n < 5 so n - 1also holds true
Hence we can use this greedy approach for this problem
'''

#I will make another function that helps to pick the best denomination
def pick_best(money) :
    if money >= 10 : return 10

    if money >= 5 : return 5

    if money >= 1 : return 1

def change(money):
    # write your code here
    #denominations : 1, 5, and 10
    if money == 0 : return 0

    count = 0

    while money != 0 :
        best_den = pick_best(money)
        money = money - best_den
        count += 1

    return count


if __name__ == '__main__':
    m = int(input())
    print(change(m))
