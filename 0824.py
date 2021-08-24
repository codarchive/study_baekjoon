#백준  2156 (포도주시식-내거,미해결)

def wineChoice(N,consnum):
    if (N,consnum) in dict_wine.keys():
        return dict_wine[(N,consnum)] 
    elif consnum==2:
        dict_wine[(N,2)]=wineChoice(N-3,2)+wineL[N-2]+wineL[N-1]
        return wineChoice(N-3,1)+wineL[N-2]+wineL[N-1]
            
    else:
        dict_wine[(N,1)]=wineChoice(N-2,2)+wineL[N-1]
        return wineChoice(N-2,2)+wineL[N-1]
import sys

N=int(sys.stdin.readline())
end=[1]*(N+1)
wineL=[int(sys.stdin.readline()) for i in range(N)]
dict_wine={(1,1):wineL[0],(1,2):wineL[0],(2,1):wineL[1],(2,2):sum(wineL[0:2])}    
print(max(wineChoice(N,2),wineChoice(N,1),wineChoice(N-1,2)))