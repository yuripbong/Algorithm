def solution(n):
    sum = 0
    if n % 2 == 0:
        for i in range(0, n+1, 2):
            i = i**2
            sum += i
    else:
        for i in range(1, n+1, 2):
            sum += i
    return sum