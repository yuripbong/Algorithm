import sys

input = sys.stdin.readline

k = int(input())
stack = []

for i in range(k):
    num = int(input())
    
    if num == 0:
        del stack[-1]
    else:
        stack.append(num)
    
print(sum(stack))
        