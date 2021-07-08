from math import *
import collections

class stat:
    def __init__(self,N,li):
        self.N=N
        self.li=li

    def sum_li(self):
        print(round(sum(self.li[0:])/N,3))
    def cen(self):
        print(li[(floor(N/2))])
    def mst_li(self):
        num_cnt=colletions.Counter(self.li)
        mst=max(self.li)
        mst_li=[]
        for num, cnt in cnt_num.items():
            if cnt== mst:
                mst_li.append(num)
        mst_li.sort()
        if len(mst_li)>1:

            print(mst_li[1])
        else:
            print(mst_li[0])

N=int(input())

li=[int(input()) for _ in range(N)]

li.sort(reverse=True)

ex=stat(N,li)

ex.sum_li()