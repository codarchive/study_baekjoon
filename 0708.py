# 백준 2108(내거)


from math import *
import collections
import sys

class stat:
    
    def __init__(self,N,li):
        self.N=N
        self.li=li
        self.collections=collections    #클래스밖의 모듈 들여올때도 이렇게 셀프 붙여서 들여와줘야함ㅋㅋ
    def sum_li(self):
        print(int(round(sum(self.li[0:])/N,0)))
    def cen(self):
        print(li[(floor(N/2))])
    def mst_li(self):
        num_cnt=self.collections.Counter(self.li)   #카운터라는거 아주 편리하군. 딕셔너리로 편리한게 많음
        mst=max(num_cnt.values())
        mst_li=[]
        for num, cnt in num_cnt.items(): #[(,),(,),(,)] 이런식으로 쌍쌍이 묶인걸 원소로 하는 리스트를 포문에 적절히 활용하면 좋음
            if cnt== mst:                       #특히 딕셔너리는 이렇게 묶여있으니까 포문에 이런식으로 활용하기 좋음.
                mst_li.append(num)
        mst_li.sort()
        if len(mst_li)>1:

            print(mst_li[1])
        else:
            print(mst_li[0])

    def rng(self):
        print(self.li[0]-self.li[-1])


N=int(input())

li=[int(sys.stdin.readline()) for _ in range(N)]

li.sort(reverse=True)


ex=stat(N,li)
ex.sum_li()
ex.cen()
ex.mst_li()
ex.rng()