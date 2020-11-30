#Finding the convex hull of the points using Graham Scan
from functools import cmp_to_key

# find the point with minimum y coordinate
def find_min_y(points):
    min_y = 999999
    min_i = 0
    for i, p in enumerate(points):
        if p[1] < min_y:
            min_y = p[1]
            min_i = i
        if p[1] == min_y:
            if p[0] < points[min_i][0]:
                min_i = i
    return points[min_i], min_i

#function for finding the orientation
def orientation(p0, p1, p2):
    o = (p1[1] - p0[1])*(p2[0] - p1[0]) - (p1[0] - p0[0])*(p2[1] - p1[1])
    return o

#function for finding the square of distance
def dist_sq(p1,p2):
    dist = ((p1[0] - p2[0])*(p1[0] - p2[0]))+((p1[1] - p2[1])*(p1[1] - p2[1]))
    return dist

# comparator for the sorting 
def polar_compare(p1, p2, p0):
    d = orientation(p0, p1, p2)
    if d < 0:
        return -1
    if d > 0:
        return 1
    if d == 0:
        if dist_sq(p1, p0) < dist_sq(p2, p0):
            return -1
        else:
            return 1

def graham_scan(points):
    # let p0 be the point with minimum y-coordinate
    p0, index = find_min_y(points)

    # swap p[0] with p[index]
    points[0], points[index] = points[index], points[0]

    # sort the points (except p0) according to the polar angle on anti-clockwise direction
    polar_sorted = sorted(points[1:], key = cmp_to_key(lambda p1, p2: polar_compare(p1, p2, p0)))
    
    
    # if more than two points are collinear with p0, keep the farthest
    remove = []
    for i in range(len(polar_sorted) - 1):
        d = orientation(polar_sorted[i], polar_sorted[i + 1], p0)
        if d == 0:
            remove.append(i)
    polar_sorted = [i for j, i in enumerate(polar_sorted) if j not in remove]

   
    m = len(polar_sorted)
    if m < 2:
        print ('The Convex hull is Empty')

    else:
        stack = []
        stack_size = 0
        stack.append(points[0])
        stack.append(polar_sorted[0])
        stack.append(polar_sorted[1])
        stack_size = 3

        for i in range(2, m):
            while (True):
                d = orientation(stack[stack_size - 2], stack[stack_size - 1], polar_sorted[i])
                if d < 0: # if it makes left turn
                    break
                else: # if it makes non left turn
                    stack.pop()
                    stack_size -= 1
            stack.append(polar_sorted[i])
            stack_size += 1
    return stack

points  = [[0, 3], [1, 1], [2, 2], [4, 4], 
                      [0, 0], [1, 2], [3, 1], [3, 3]];

n = len(points)/len(points[0]);
print (graham_scan(points) )
