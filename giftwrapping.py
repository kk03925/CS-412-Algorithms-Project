
import matplotlib.pyplot as plt  
import random
import DataGeneration as DataGeneration
import plotting


def left_most_point(list_of_points):
    left_point=0
    for i in range(len(list_of_points)-1):
      
        if list_of_points[i][0] <= list_of_points[left_point][0]:
            minn = i
    return left_point

def orientation(p,q,r):

    ''' val = 2 shows counterclockwise
        val = 1 shows clockwise '''
    val = 0
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val < 0:
        return 2
    
    elif val >0 :
        return 1

def gift_wrapping( list_of_points):
    if len(list_of_points) < 3:
        return 'there cannot be a convex hull of this list of points'
    n = len(list_of_points)
    l = 0
    l = left_most_point(list_of_points)
    list_of_convexhull_points = []
    q = 0
    p = 0
    p = l
    while ( True):
        list_of_convexhull_points.append(p)
        q = (p+1)%n
        for i in range(len(list_of_points)):
            val_condition = orientation(list_of_points[p],list_of_points[i], list_of_points[q])
            if val_condition ==2:
                q = i
        
        p = q
        if p==l:
            break  

    tuple_of_hull_points= []
    for i in list_of_convexhull_points:
        print(list_of_points[i][0] , list_of_points[i][1])
        tuple_of_hull_points.append((list_of_points[i][0] , list_of_points[i][1]))
    return tuple_of_hull_points



def main():

    dict_of_all_points=  DataGeneration.DataGeneration()

    #dict_of_all_points[100] gives us list of 100 tuples
    #dict_of_all_points[100] is a list_of_points

    #display func has 2 arg: 1) list_of_points=all points , 2)list of hull points
    plotting.display (dict_of_all_points[200], [])  #this plots a graph for all points

    hull_points_list = gift_wrapping(dict_of_all_points[200]) #gift_wrapping returns us a list of tuples of hullpoints
    
    plotting.display (dict_of_all_points[200], hull_points_list) #plots the final graph with hull points

if __name__ == "__main__":
    main()
