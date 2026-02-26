import sys

input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    cmd = list(map(int, input().split()))
 
    if cmd[0] == 1:
        stack.append(cmd[1]) # 정수 X를 스택에 넣는다.
    elif cmd[0] == 2:
        if len(stack) == 0: # 스택이 빈 경우
            print(-1)       # -1 출력
        else:
            print(stack[-1])
            del stack[-1]     # 스택 마지막 원소 빼고 출력
    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    
    