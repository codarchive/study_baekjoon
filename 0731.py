#백준 14889(내거)

N= int(input())
S_mat={i:list(map(int,input().split())) for i in range(N)}
team_set=[]
team=[0]*int(N/2)
srt=1
def teamMem(k=0):
    import copy
    global team_set
    global team
    global srt
    
    if k==N/2 and 0 not in team:
        team_set.append(copy.copy(team))
        
    else:
        for i in range(srt,N+1):
            if i not in team[0:k]:
                k+=1
                team[k-1]=i 
                
                srt=i
           
              
                teamMem(k)
                k-=1
teamMem()

def getScore(team):
    score=0
    for i in team:
        for j in team:
            if j!= i:
                score+=S_mat[i-1][j-1]
    return score

dif_score=dict()
i=1

for s_mem in team_set:
    s_score=getScore(s_mem)
    r_mem=list(set(range(1,N+1))-set(s_mem))
    r_score=getScore(r_mem)
    dif_score[i]=abs(int(s_score)-int(r_score))
    i+=1

print(min(list(dif_score.values())))