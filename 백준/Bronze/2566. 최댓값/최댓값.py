arr = []

for i in range(9):
    arr.append(list(map(int, input().split())))
    
m = 0
row = 0
col = 0

for i in range(9):
    if max(arr[i]) > m:
        m = max(arr[i])
        row = i
        col = arr[i].index(max(arr[i]))
    
print(m)
print(row+1, col+1)