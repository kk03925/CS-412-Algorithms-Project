import DataGeneration as DataGeneration
import plotting


def findSide (p_1,p_2,p):
  side_val = ((p[1] - p_1[1])*(p_2[0] - p_1[0])) - ((p_2[1] - p_1[1])*(p[0] - p_1[0]))
  if side_val > 0:
    return 1
  elif side_val < 0:
    return -1
  return 0

def lineDist (p_1,p_2,p):
  side_val = ((p[1] - p_1[1])*(p_2[0] - p_1[0])) - ((p_2[1] - p_1[1])*(p[0] - p_1[0]))
  return abs(side_val)

class quickHull:
  point_lst = []
  finalHull = []

  def __init__(self,input_lst):
    self.point_lst = input_lst


  def quickHullHelper(self,p_1,p_2,pointSide):

    index = -1
    max_dist = 0


    for i in range(len(self.point_lst)):
      val = lineDist(p_1,p_2,self.point_lst[i])
      if ( (findSide(p_1,p_2,self.point_lst[i]) == pointSide) and val > max_dist ):
        index = i
        max_dist = val

    if (index == -1):
      if (p_1 not in self.finalHull):
        self.finalHull.append(p_1)
      if (p_2 not in self.finalHull):
        self.finalHull.append(p_2)
      #print(self.finalHull)
      return
    
    a = self.point_lst[index]
    
    self.quickHullHelper(a,p_1, -1*(findSide(a,p_1,p_2)))
    self.quickHullHelper(a,p_2, -1*(findSide(a,p_2,p_1)))

    



  def quickHull(self):
    n = len(self.point_lst)

    if n<3:
      return

    
    x_min, x_max = 0,0
    for i in range(1,n):
      if (self.point_lst[i][0] < self.point_lst[x_min][0]):
        x_min = i
      if (self.point_lst[i][0] > self.point_lst[x_max][0]):
        x_max = i


    a = self.point_lst[x_min]
    b = self.point_lst[x_max]

    self.quickHullHelper(a,b,1)

    self.quickHullHelper(a,b,-1)

    


def main():

    dict_of_all_points=  DataGeneration.DataGeneration()
     
    #dict_of_all_points[100] gives us list of 100 tuples
    #dict_of_all_points[100] is a list_of_points

    #display func has 2 arg: 1) list_of_points=all points , 2)list of hull points
    #plotting.display ([(0,3),(1,1),(2,2),(4,4),(0,0),(1,2),(3,1),(3,3)], [])  #this plots a graph for all points

    quickHullObj = quickHull(dict_of_all_points[10])

    

    #quickHullObj = quickHull(dict_of_all_points[10]) #gift_wrapping returns us a list of tuples of hullpoints
    quickHullObj.quickHull()
    hull_points_list = quickHullObj.finalHull
    print(hull_points_list)
    #plotting.display ([(0,3),(1,1),(2,2),(4,4),(0,0),(1,2),(3,1),(3,3)], hull_points_list) #plots the final graph with hull points

if __name__ == "__main__":
    main()


  


  
