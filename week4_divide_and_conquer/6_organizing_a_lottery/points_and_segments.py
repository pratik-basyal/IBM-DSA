from sys import stdin


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

#Function to search return result for base case
def base_case(segments, points) :
    result = [0] * len(points)
    for i, point in enumerate(points) :
        for segment in segments :
            if segment[0] <= point and segment[1] >= point :
               result[i] += 1

            elif segment[0] > point : break
    return result

#Divide and Conquer Approach : 
def divide_and_conquer(segments, points) :
    #base case for recursion
    if(len(segments) == 1 or len(points) == 1) :
        return base_case(segments, points)

    mid_seg = len(segments) // 2
    mid_point = len(points) // 2

    left_points = points[: mid_point]
    right_points = points[mid_point :]

    left_segments = segments[: mid_seg]
    right_segments = segments[mid_seg : ]

    left_half = divide_and_conquer(left_segments, left_points)
    right_half = divide_and_conquer(right_segments, right_points)

    return merge(left_half, right_half, left_points, right_points, left_segments, right_segments)

def merge(left_result, right_result, left_points, right_points, left_segments, right_segments):
    result = []
    
    result.extend(left_result)
    result.extend(right_result)

    #checking if theres any overlapping segments on the right segments for left points
    for i, point in enumerate(left_points) :
        j = 0 #pointer to right segments
        while(j < len(right_segments) and point >= right_segments[j][0]) :
            if(right_segments[j][0] <= point <= right_segments[j][1]) :
                result[i] += 1
            j += 1

    #checking if theres any overlapping segments on the left segments for right points
    for i, point in enumerate(right_points, start = len(left_segments)) :
        
        j = len(left_segments) #pointer to left segments
        while(j < len(left_segments) and point >= left_segments[j][0]) :
            if(left_segments[j][0] <= point <= left_segments[j][1]) :
                result[i] += 1
            j -= 1

    return result
    

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    segments = [(data[i], data[i+1]) for i in range(2, 2 * n + 2, 2)]
    points = data[2 * n + 2:]

    segments.sort(key=lambda x: x[0])  # Sorting segments by starting points
    indexed_points = sorted(enumerate(points), key=lambda x: x[1])  # Sorting points with original indices
    sorted_points = [point for index, point in indexed_points]

    #print(sorted_points)

    output_count = divide_and_conquer(segments, sorted_points)

    #print(indexed_points)

    # Restoring original order of points
    final_output = [0] * m
    for i, (index, _) in enumerate(indexed_points):
        final_output[index] = output_count[i]

    print(*final_output)
