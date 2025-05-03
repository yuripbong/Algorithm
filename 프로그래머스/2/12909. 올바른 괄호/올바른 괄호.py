def solution(s):
    answer = True
    s_list = list(s)
    bracket = []
    
    for i in range(len(s)):
        if s_list[i] == "(":
            bracket.append(s_list[i])
        elif s_list[i] == ")":
            if not bracket:
                answer = False
                break
            else:
                bracket.pop()
    if len(bracket) > 0:
        answer = False
    return answer