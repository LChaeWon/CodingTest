for test_case in range(10):
    N = int(input())
    M = [list(map(int,input().split())) for _ in range(100)]

    m = 0
    c = 0
    d = 0
    for i in range(100):
        a = 0
        b = 0

        for j in range(100):
            a += (M[i][j])
            b += (M[j][i])
        m = max(m, a, b)
        c += M[i][i]
        d += M[i][99-i]
    print(f"#{test_case+1} {max(m,c,d)}")






