
# 백준 2750(내거)

N=int(input())

li= [*map(int,[input() for _ in range(N)])]

li.sort()

for i in range(N):
    print(li[i])
