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
    flag = True # if false found lowest
    best = sum_items(A)
    while flag:
        flag = False
        
    
    
    
    
    
    return best
    # write your code in Python 3.6
    pass
