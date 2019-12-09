from copy import copy

def solution(A, B, C):
    found = []
    for i,item in enumerate(A):
        for index,value in enumerate(C):
            if A[i]<=value and B[i]>=value:
                # if index in found:
                #     break
                # else:
                found.append(index)
                break
    return len(found)

def check(lower:int,higher:int,C:list,beg:int,end:int)->(int,int,int):
    candidate = (beg+end)//2
    if lower<=C[candidate]<=higher:
        return 0,0,candidate
    if C[candidate]<lower:
        return candidate,end,None
    if C[candidate]>higher:
        return beg,candidate,None


def solution2(A, B, C):
    C.sort()
    founds = []
    not_found = False
    for i,item in enumerate(A):
        lower = A[i]
        higher = B[i]
        beg = 0
        end = len(C)
        found = None
        while found==None:
            beg,end, found = check(lower,higher,C,beg,end)
            if beg==end and found ==None:
                not_found = True
                break
            if found:
                founds.append(found)
    if not not_found:
        return len(set(founds))
    else:
        return -1


a = solution2([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2])
print(a)
