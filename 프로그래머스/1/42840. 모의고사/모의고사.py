def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ss1 = 0
    ss2 = 0
    ss3 = 0
    r = []
    i1 = 0
    i2 = 0
    i3 = 0
    
    for i in range(len(answers)):
        if i1 == 5:
            i1 = 0
        if i2 == 8:
            i2 = 0
        if i3 == 10:
            i3 = 0
        if answers[i] == s1[i1]:
            ss1 += 1
        if answers[i] == s2[i2]:
            ss2 += 1
        if answers[i] == s3[i3]:
            ss3 += 1
        i1 += 1
        i2 += 1
        i3 += 1
    
    if len(answers) == ss1:
        print('수포자 1은 모든 문제를 맞혔습니다.')
    elif ss1 == 0:
        print('수포자 1은 모든 문제를 틀렸습니다.')
    if len(answers) == ss2:
        print('수포자 2는 모든 문제를 맞혔습니다.')
    elif ss2 == 0:
        print('수포자 2는 모든 문제를 틀렸습니다.')
    if len(answers) == ss3:
        print('수포자 3은 모든 문제를 맞혔습니다.')
    elif ss3 == 0:
        print('수포자 3은 모든 문제를 틀렸습니다.')
        
    if ss1 == ss2 and ss1 == ss3:
        print(f'모든 사람이 {ss1}문제씩을 맞췄습니다.')
        return [1, 2, 3]
    
    result = sorted([ss1, ss2, ss3], reverse=True)
    
    # 점수와 번호를 함께 묶고 정렬
    score_list = [(1, ss1), (2, ss2), (3, ss3)]
    score_list.sort(key=lambda x: x[1], reverse=True)

    # 점수가 같은 사람도 포함하되, 중복 없이 순서대로
    max_score = score_list[0][1]
    for person, score in score_list:
        if score == max_score:
            r.append(person)
        elif score < max_score:
            break
            
    return r
