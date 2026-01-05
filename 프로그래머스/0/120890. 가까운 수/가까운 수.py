def solution(array, n):
    num = array[0]
    for i in range(1, len(array)):
        if abs(num-n) > abs(array[i]-n):
            num = array[i]
        elif abs(num-n) == abs(array[i]-n):
            num = min(num, array[i])

    return num