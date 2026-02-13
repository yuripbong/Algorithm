n = int(input())

tmp = len(str(n))
tmp = sum(map(int, '9' * tmp))

answer = 0
for i in range(max(0, n - tmp), n):
    if (sum(map(int, str(i))) + i) == n:
        answer = i
        break
    
print(answer)
