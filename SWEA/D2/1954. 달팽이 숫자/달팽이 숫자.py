T = int(input())
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
for i in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    r, c = 0, 0
    d = 0
    for j in range(1, N*N+1):
        snail[r][c] = j
        r += row[d]
        c += col[d]

        if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0:
            r -= row[d]
            c -= col[d]
            d = (d + 1) % 4

            r += row[d]
            c += col[d]
    print("#{}".format(i))
    for k in range(N):
        for l in range(N):
            print(snail[k][l],end=" ")
        print()
