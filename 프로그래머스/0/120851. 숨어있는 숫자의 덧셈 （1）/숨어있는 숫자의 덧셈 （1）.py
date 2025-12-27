def solution(my_string):
    answer = ([int(i) for i in my_string if (i in '0123456789')])
    
    return sum(answer)