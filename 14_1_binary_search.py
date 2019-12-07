# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from functools import reduce
def sum_items(A):
    return reduce(lambda x,y: x+y,A)

def solution(K, M, A):
    # K - count of blocks
    # M -  biggest element in A
    elements_size = [0]*K
    blocks = [[]]*K
    A_len = len(A)
    print(A_len)
    flag = True # if false found lowest
    best = sum_items(A)
    best_possible = int(best/K)
    first_size = 1
    total_sum_best = 100000000000000000000
    for j in range(K-1):
        for i in range(1,A_len):
            print(f"\n\ni:{i}")
            best_block = A[0:i]
            rest_block = A[i:]
            best_block_sum = sum_items(best_block)
            rest_block_sum = sum_items(rest_block)/(K-1-j)
            total_sum = best_block_sum + rest_block_sum
            print(f"best_block:{best_block}\nbest_blokc_sum:{best_block_sum}")
            print(f"rest_block:{rest_block}\nrest_blokc_sum:{rest_block_sum}")
            print(f"total = {total_sum}")
            if total_sum < total_sum_best:
                total_sum_best = total_sum
                block_to_sub = i
                print(f"new block to sub:{block_to_sub}")
        A = A[block_to_sub:]
        print(f"\n####\nnew A:{A}")
        A_len = len(A)


    return best
    # write your code in Python 3.6
    pass

a =solution(3,5,[2,1,5,1,2,2,2])
print("#\n######\n####")
print(a)