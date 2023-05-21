n = int(input())
x = [[0] * 0 for a in range(n)]
for i in range(n):
    line = input().split()
    for j in range(len(line)):
        x[i].append(int(line[j]))
for i in range(n):
    for j in range(n):
        #第一种关系
        if j== 0 and i==0:
            x[i][j] = x[i][j]
        #第二种关系
        elif j == 0:
            x[i][j] = x[i][j] + x[i - 1][j]
        #第二种关系
        elif i == 0:
            x[i][j] = x[i][j] + x[i][j - 1]
        #第三种关系
        else:
            x[i][j] = max(x[i][j - 1],x[i - 1][j])+ x[i][j]
print(x[n-1][n-1])
