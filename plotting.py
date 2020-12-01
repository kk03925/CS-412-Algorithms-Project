import matplotlib.pyplot as plt  
def display (list_of_points, lst):
    
    x = [p[0] for p in list_of_points]
    y = [p[1] for p in list_of_points]
    plt.plot(x,y, marker = 'D', linestyle = 'None')
    if lst!= []:

        lst.append(lst[0])
        hx= [p[0] for p in lst]
        
        hy= [p[1] for p in lst]
        plt.plot(hx,hy)
    plt.title('convex hull')
    plt.show()

    

