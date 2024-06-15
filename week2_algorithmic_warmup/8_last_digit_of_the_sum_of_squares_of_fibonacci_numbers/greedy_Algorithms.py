#problem description : Celebration Party Problem
'''
Many children came to the party. We need to organize them in minimum possible number of groups
such that age of any two children on that group differs at most by 2 years
'''

#Approach : 
'''
We will use sorting and greedy approach
i. First we will sort the children with their ages
ii. We will take segment technique, where each segment is of length 2 years
iii. We will use each segment from left most number of children's age and try to cover everything with segments
iv. number of segments will be the number of groups and that will be minimum possible number of groups
'''

def celebration_party(children) :
    if not children :
        return 0
    
    children.sort() #-- this will take O(nlogn)
    
    segment = 1 #at least one child will be there
    starting_segment = children[0]

    for age in children :
        if(age - starting_segment >= 2) :
            segment += 1
            starting_segment = age
    
    return segment


#problem description : 
'''
A thief has a a knapsack of weight W. He wants to maximize his loot from the items with
value v_1, and weight w_1.
We will use Greedy Approach.
'''

#Approach : 
'''
First we will find the best item from the items i.e. max (value / weight)
We will add max weight of this item to knapsack
if knapsack is not full, we will go to remaining items
And again repeat the same process for the sub problems
Ultimately we are doing this greedy approach
'''

#So first we need to find the best item so we are creating different function to make it easier :
def bestItem(items) :
    if not items :
        return 0
    
    n = len(items)
    best_item = 0
    max_value = 0

    for i in range(n) :
        value_i = items[i][0]
        weight_i = items[i][1]
        if weight_i > 0 : #weight
            if(value_i / weight_i > max_value) :
                max_value = value_i / weight_i
                best_item = i

    return best_item

#Items will be given in array of tuples
def max_loot(items, W) :
    #tuple is stored as v_1 and w_1 format

    if W == 0 :
        return 0
    
    loot = 0

    while W != 0 and items :
    
        #first we will get index of best item from prev func
        best_item = bestItem(items)

        value_i = items[best_item][0]

        #unit price of best_item
        unit = items[best_item][0] // items[best_item][1]

        #fill that in the knapsack of total W
        w_i = items[best_item][1]

        if(w_i > W) :
            return unit * W #this will be the max loot
        
        loot += value_i

        W = W - w_i

        del items[best_item]

    #For this problem overall runtime is O(n^2) but we can sort the items with value / weight in decreasing order first
    # Then we can optimize the runtime with O(nlogn)
