def solution(a, b):
    s = 2*a*b
    sum = str(a) + str(b)
    sum1 = int(sum)
    return max(s, sum1)