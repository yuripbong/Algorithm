from math import ceil

n = input()
s = ceil(len(n)/10)

for i in range(s):
    for j in range(10):
        index = i*10+j
        if index >= len(n):
            break
        print(n[index], end="")
    print()
