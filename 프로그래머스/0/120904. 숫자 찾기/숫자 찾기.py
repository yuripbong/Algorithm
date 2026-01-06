def solution(num, k):
    answer = -1
    
    s_num = str(num)
    if str(k) in s_num:
        answer = s_num.index(str(k)) + 1
    return answer