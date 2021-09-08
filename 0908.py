#백준  1931 (회의실배정-내거)

import sys
N=int(sys.stdin.readline())
times=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
times.sort(key=lambda x: x[1])
meetTimes=[[0,0]]
switch=True
while switch:
    for time in times:
        switch=False
        if time[0]>=meetTimes[-1][1]:
            meetTimes.append(time)
            switch=True
            break
print(len(meetTimes)-1)