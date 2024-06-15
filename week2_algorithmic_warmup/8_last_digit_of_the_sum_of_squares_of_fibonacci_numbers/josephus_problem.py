'''
Description of the Josephus problem : 
Given n number of people and k as position where person gets killed
We need to find the position of the survivor.
The first person to get killed is k - 1 th position
After that the position shifted by k and that person is killed until theres only one person left
'''

def josephus(n, k) :
    #going with recursion
    #when k - 1th person is killed we will have  n-1 people
    #now (josephus(n,k) + k)th person is killed
    #to do it within a cycle we will do mod n

    #base case
    if n == 1 : return 0 #if theres only one survivor

    return (josephus(n-1, k) + 3) % n


#Maximizing salary problem
#Approach : Greedy Algorithm
'''
Description : Boss gives you array of an integer and wants you to rearrange those numbers and that number will be your salary
We will definitely want to get max salar so
'''
def maximize_Salary(array) :
    #find maximum number from array and remove it from it
    #we append it on another array, and we will remove from original
    result = []

    while (array != []) :
        max_ = max(array)
        result.append(max_)
        array.remove(max_)
    
    return result

if __name__ == '__main__' :
   #n,k = map(int, input().split())
   #print(josephus(n, k))
   print(maximize_Salary([1,4,9,8,9,7]))


