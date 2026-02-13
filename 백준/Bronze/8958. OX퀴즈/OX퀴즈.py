case = int(input())

for i in range(case):
    test = input()
    
    tmp = 0
    score = 0
    
    for j in range(len(test)):
        if test[j] == "O":
            tmp += 1
            score += tmp
        elif test[j] == "X":
            tmp = 0
    print(score)
