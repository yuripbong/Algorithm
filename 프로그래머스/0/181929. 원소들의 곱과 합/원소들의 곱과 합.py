def solution(num_list):
    answer = 0
    mul = 1
    sum = 0
    for i in range(len(num_list)):
        sum += num_list[i]
        mul *= num_list[i]
    if mul < sum**2:
        answer = 1
    else:
        answer = 0
    return answer