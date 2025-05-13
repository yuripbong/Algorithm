import math

def solution(array):
    answer = 0
    array.sort()
    answer = array[math.floor(len(array)/2)]
    
    return answer