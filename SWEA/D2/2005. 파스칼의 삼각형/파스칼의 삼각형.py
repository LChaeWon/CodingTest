T = int(input())
for k in range(1, T+1):
    N = int(input())
    a = []
    for i in range(N):
        a.append([])
        for j in range(0, i+1):
            if j == 0 or j == i:
                a[i].append(1)
            else:
                a[i].append(a[i-1][j-1]+a[i-1][j])
    print(f"#{k}")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()
