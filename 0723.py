N = int(input())
coord_set=[]
coord=[]
dontGo=[]
line=1
def Q_cord():
    global coord
    global line
    for i in range(1,N+1):
    
        if set(coord[n][1] for n in range(len(coord)))!=0:
            if (abs(coord[k][0]-line) != abs(coord[k][1]-i) for k in range(len(coord))) :
                coord.append((line,i))
                
                if len(coord)==N:
                    coord_set.append(coord)
                    coord=[]
                    line=1
                else:
                    line+=1
                    Q_cord()
        



            


Q_cord()
