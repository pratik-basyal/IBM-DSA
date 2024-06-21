from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

#Approach : 
'''
Will use greedy approach
1. Sort the tuple of intervals with its ending point, in ascending order
2. We itereate,  through each interval
3. We choose the first and remove every conflicting intervals, and if its not conflicting we pick end point again
4. We add the end point to the array of points
5 Finally we return points
'''
def optimal_points(segments):
    segments.sort(key = lambda x : x[1])

    points = [segments[0][1]]
    i = 0 #pointer to current endpoint
    # write your code here
    for j in range(1, len(segments)):
        s = segments[j]
        
        if points[i] >= s.start and points[i] <= s.end : continue

        else :
            points.append(s.end)
            i += 1 
            

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #print(segments)
    points = optimal_points(segments)
    print(len(points))
    print(*points)

'''
3
1 3
2 5
3 6
'''