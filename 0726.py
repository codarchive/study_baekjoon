
#백준 9663(내거-실패)

N = int(input())
coord_set=[]
coord=[]
line=1

def Q_cord():
    global coord
    global line
 
    for i in range(1,N+1):
        if line==N:
            coord=[]
            line=1
            if len(coord)==N:
                coord_set.append(coord)
            else:
                continue
            
        
        else:

            if (len({i}-set(coord[n][1] for n in range(len(coord)))))!=0 and (True not in list(abs(coord[k][0]-line) == abs(coord[k][1]-i) for k in range(len(coord)))):
                coord.append((line,i))
                line+=1
                print("Q_cord")
                Q_cord()
       
   


            


Q_cord()