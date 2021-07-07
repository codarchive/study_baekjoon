
from math import *
import sys

N=int(sys.stdin.readline())

def up_dn(a,li,left,right):

    idx=floor((left+right)/2)

    if right-left<=1:

        if li[right]<a:
            li.append(a)
        elif li[left]>a:
            li.insert(left,a)
        else:
            li.insert(right,a)
                
    else:

        if a> idx:
            up_dn(a,li,idx,right)

            
        else:
            up_dn(a,li,left,idx)
