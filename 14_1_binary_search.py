# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from functools import reduce
def sum_items(A):
    if len(A)==0:
        return 0
    else:
        return reduce(lambda x,y: x+y,A)

def solution(K, M, A):
    # K - count of blocks
    # M -  biggest element in A
    elements_size = [0]*K
    blocks = [[]]*K
    A_len = len(A)
    print(A_len)
    curr_metric = 1000000000000
    flag = True # if false found lowest
    for i in range(A_len+1):
        try:
            first_block = A[0:i]
            sum_first_block = sum_items(first_block)
            avg_first_block = sum_first_block/i

            end_block = A[i:]
            sum_end_block = sum_items(end_block)
            avg_end_block = sum_end_block/(A_len-i)
            metric = avg_first_block/avg_end_block

            print(f"beg :{first_block} :sum {sum_first_block} avg {avg_first_block}")
            print(f"end :{end_block}  :sum {sum_end_block} avg {avg_end_block}")
            print(f"{metric}")
            
            if metric <curr_metric:
                curr_metric=metric
                print(f"current best ={first_block}")
                best = first_block
        except:
            pass
        print("\n")
    print(f"best :{best}")


    return best
    # write your code in Python 3.6
    pass

a =solution(3,5,[2,1,5,1,2,2,2])
print("#\n######\n####")
print(a)