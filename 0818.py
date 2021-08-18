# 백준 2579 계단오르기 (내거)

def stair(floor=1,step=1):
    if (floor,step) in stairs.keys():
        return stairs[(floor,step)]
    if step==2:
        stairs[(floor,2)]=max(stair(floor-2,1),stair(floor-2,2))+score[floor]
        return max(stair(floor-2,1),stair(floor-2,2))+score[floor]
    else:
        stairs[(floor,1)]=stair(floor-1,2)+score[floor]
        return stair(floor-1,2)+score[floor]
import sys
N=int(sys.stdin.readline())
score={i+1:int(input()) for i in range(N)}
stairs={(0,1):0,(0,2):0,(1,1):score[1],(1,2):score[1]}
print(max(stair(N,1),stair(N,2)))