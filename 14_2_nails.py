def check(lower:int,higher:int,C:list,beg:int,end:int)->(int,int,int):
    candidate = (beg+end)//2
    if lower<=C[candidate]<=higher:
        return 0,0,candidate
    if C[candidate]<lower:
        return candidate,end,None
    if C[candidate]>higher:
        return beg,candidate,None


def solution(A, B, C):
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

def can_be_nailed(AB_to_check,nail):
    if AB_to_check[0]<=nail<=AB_to_check[1]:
        return True
    else:
        return False

def check_nailed(AB,nail):
    beg = 0
    end = len(AB)
    nailed = []
    direction = 0
    prev_candiate =10000000000000000
    while beg<=end:
        candidate = (beg+end+direction)//2
        if prev_candiate == candidate:
            if nailed:
                return nailed
            else:
                return []
        AB_to_check = AB[candidate]
        if nail <AB_to_check[0]:
            end = candidate
            direction = -1
            continue
        if nail > AB_to_check[1]:
            beg = candidate
            direction = +1
            continue
        if can_be_nailed(AB_to_check,nail):
            nailed.append(candidate)
            prev_candiate = candidate
            if direction ==-1 and candidate ==0:
                direction = 1
            if direction == 1 and candidate == len(AB):
                direction = -1

    pass

def check_if_all_nailed(nailed_list,plank_count):
    for i in range(plank_count):
        if i not in nailed_list:
            return False
    return True

def solution(A,B,C):
    AB = list(zip(A,B))
    plank_count = len(A)
    counter = 0
    nailed_list = []
    for nail in C:
        nailed_list=nailed_list+check_nailed(AB,nail)
        if check_if_all_nailed(nailed_list,plank_count):
            return len(set(nailed_list))
        else:
            continue
    return -1



    
        



a = solution([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2])
print(a)
