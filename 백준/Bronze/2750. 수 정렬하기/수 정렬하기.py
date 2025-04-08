n = int(input())
s_list = []

for i in range(n):
    s = int(input())
    s_list.append(s)

for i in range(n):
    for j in range(i + 1, n):
        if s_list[i] > s_list[j]:
            s_list[i], s_list[j] = s_list[j], s_list[i]

for i in range(n):
    print(s_list[i])
