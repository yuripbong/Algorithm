def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    answer = a % 1234567
    return answer
