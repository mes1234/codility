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

def solution2(A, B, C):
    C_sorted = C.sort()
    found = []
    for i,item in enumerate(A):
        lower = A[i]
        higher = B[i]
        candidate = len(C_sorted)
        beg = C_sorted[0]
        end = C_sorted[:-1]
        while beg <= end:
            beg,end = check(lower,higher,beg,end,C_sorted)


a = solution2([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2])
print(a)