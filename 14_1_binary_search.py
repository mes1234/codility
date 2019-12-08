# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from functools import reduce
def sum_items(A):
    if len(A)==0:
        return 0
    else:
        return reduce(lambda x,y: x+y,A)

def solution(K, M, A):
    for j in range(K):
        curr_metric = 1000000000000
        A_len = len(A)
        for i in range(A_len+1):
            try:
                first_block = A[0:i]
                sum_first_block = sum_items(first_block)
                avg_first_block = sum_first_block/i

                end_block = A[i:]
                sum_end_block = sum_items(end_block)
                avg_end_block = sum_end_block/(A_len-i)
                metric = avg_first_block/avg_end_block

                # print(f"beg :{first_block} :sum {sum_first_block} avg {avg_first_block}")
                # print(f"end :{end_block}  :sum {sum_end_block} avg {avg_end_block}")
                # print(f"{metric}")
                
                if metric <curr_metric:
                    curr_metric=metric
                    # print(f"current best ={first_block}")
                    best = first_block
            except:
                pass
            print("\n")
            print(f"best :{best}")
        A= A[i:]

    return best
    # write your code in Python 3.6
    pass

def solution1(K, M, A):
    # K block count
    # M max element
    # A list
    min_max = 100000000000000000000000
    for counter,item in enumerate(A):
        if item == M:
            try:
                if M+A[counter+1] < min_max:
                    min_max = M+A[counter+1]
                if M+A[counter-1]< min_max:
                    min_max = M+A[counter-1]
            except:
                pass
    print(min_max)
    return min_max

def calc(A:list,prev_best:int,K:int, base_item:int)->int:
    items = [[]]*K
    current_index =0
    for i in range(K):
        if i ==K-1:
            items[i]=A[current_index:]
        else:
            items[i]= A[i:base_item+current_index]
        current_index = base_item+current_index
        

    k=K-1
    



def solution3(K,M,A):
    B =1
    for j in range(len(A)-2):
        items = [[]]*K
        for i  in range(K):
            if i == 0:
                items[i] = A[:B]
            if i == K-1:
                items[i] = A[B+i+j-1:]
            else:
                items[i] = A[i:i+j]
        pass

def blockSizeIsValid(A, max_block_cnt, max_block_size):
    block_sum = 0
    block_cnt = 0
 
    for element in A:
        if block_sum + element > max_block_size:
            block_sum = element
            block_cnt += 1
        else:
            block_sum += element
        if block_cnt >= max_block_cnt:
            return False
 
    return True
 
def binarySearch(A, max_block_cnt, using_M_will_give_you_wrong_results):
    lower_bound = max(A)
    upper_bound = sum(A)
 
    if max_block_cnt == 1:      return upper_bound
    if max_block_cnt >= len(A): return lower_bound
 
    while lower_bound <= upper_bound:
        candidate_mid = (lower_bound + upper_bound) // 2
        if blockSizeIsValid(A, max_block_cnt, candidate_mid):
            upper_bound = candidate_mid - 1
        else:
            lower_bound = candidate_mid + 1
 
    return lower_bound
 
def solution(K, M, A):
    return binarySearch(A,K,M)

    best_sum = calc(A,10000000,K,1)



a =solution(3,5,[2,1,5,1,2,2,2])
# a =solution(3,5,[5,1,2,2,2])
print("#\n######\n####")
print(a)