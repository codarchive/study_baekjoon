#백준  11047 (동전0-내거)

N,K = map(int,input().split())
coins=[int(input()) for _ in range(N)]

coins.sort(reverse=True)
cnt=0
for i in coins:
    if K//i>=1:
        cnt+=K//i
        K=K%i

print(cnt)