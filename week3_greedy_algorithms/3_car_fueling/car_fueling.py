from sys import stdin


#Approach : 
'''
We can use simple greedy algorithm in this soution
We choose stop with max distance that a car can go with full tank
We can prove that this greedy approach provides optimal solution, becasue
If we take stop with more distance than tank, then we can't travel since car can't go that far
If we take stop with less distance than current stop, then it adds fills which is not necessary
'''
def min_refills(distance, tank, stops):
    # write your code here
    tank_d = tank
    distance_travelled = 0 #car hasn't started yet
    refill = 0

    for stop in stops :
        if(distance - distance_travelled) <= tank_d : return refill

        elif stop - distance_travelled <= tank_d :
            tank_d -= (stop - distance_travelled)
            distance_travelled += (stop - distance_travelled)
        
        else :
            refill += 1
            tank_d = tank
            
            if(stop - distance_travelled <= tank_d) :
                tank_d -= (stop - distance_travelled)
                distance_travelled += (stop - distance_travelled)

            else : return -1
        
        
    if(tank_d < distance - distance_travelled) : 
        refill +=1
        tank_d = tank

        if(tank_d < distance - distance_travelled) : return -1
        

    return int (refill)


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
