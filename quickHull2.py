import DataGeneration as DataGeneration
import plotting

def findSide (p_1,p_2,p):
  side_val = (p[1] - p_1[1])*(p_2[0] - p_1[0]) - (p_2[1] - p_1[1])*(p[0] - p_1[0])
  if side_val > 0:
    return 1
  elif side_val < 0:
    return -1
  return 0

def lineDist (p_1,p_2,p):
  side_val = (p[1] - p_1[1])*(p_2[0] - p_1[0]) - (p_2[1] - p_1[1])*(p[0] - p_1[0])
  return abs(side_val)



def quickHullHelper(point_lst,n,p_1,p_2,pointSide,finalHull):

  index = -1
  max_dist = 0

  for i in range(n):
    val = lineDist(p_1,p_2,point_lst[i])
    if ( (findSide(p_1,p_2,point_lst[i]) == pointSide) and val > max_dist ):
      index = i
      max_dist = val

  if (ind == -1):
    finalHull.append(p_1)
    finalHull.append(p_2)
    return finalHull
  
  a = quickHullHelper(point_lst,len(point_lst),point_lst[ind],p_1, -1*(findSide(point_lst[ind],p_1,p_2)),finalHull)
  b = quickHullHelper(point_lst,len(point_lst),point_lst[ind],p_2, -1*(findSide(point_lst[ind],p_2,p_1)),a)

  return b



def quickHull(point_lst):
  finalHull = []
  n = len(point_lst)

  if n<3:
    return

  
  x_min, x_max = 0,0
  for i in range(1,len(point_lst)):
    if (point_lst[i][0] < point_lst[x_min][0]):
      x_min = i
    if (point_lst[i][0] > point_lst[x_max][0]):
      x_max = i
      

  a = quickHullHelper(point_lst,len(point_lst),point_lst[x_min],point_lst[x_max],1,finalHull)

  b = quickHullHelper(point_lst,len(point_lst),point_lst[x_min],point_lst[x_max],-1,a)

  return b


def main():

    dict_of_all_points=  DataGeneration.DataGeneration()

    #dict_of_all_points[100] gives us list of 100 tuples
    #dict_of_all_points[100] is a list_of_points

    #display func has 2 arg: 1) list_of_points=all points , 2)list of hull points
    plotting.display (dict_of_all_points[700], [])  #this plots a graph for all points

    hull_points_list = quickHull(dict_of_all_points[700]) #gift_wrapping returns us a list of tuples of hullpoints
    #print(hull_points_list)
    plotting.display (dict_of_all_points[700], hull_points_list) #plots the final graph with hull points

if __name__ == "__main__":
    main()


  


  