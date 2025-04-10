import sys

n = int(input())
arr = []

for _ in range(n):
    s = int(sys.stdin.readline())
    arr.append(s)

arr.sort()
    
for i in range(n):
    print(arr[i])
