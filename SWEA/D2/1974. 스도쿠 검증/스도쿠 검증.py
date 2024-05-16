T = int(input())
for test_case in range(1,T+1):
    S = [list(map(int,input().split())) for _ in range(9)]

    result = 1
    for i in range(9):
        row = [0]*10
        com = [0]*10
        for j in range(9):
            row[S[i][j]] += 1
            com[S[j][i]] += 1
        for k in range(1,10):
            if row[k] != 1:
                result = 0
                break
            if com[k] != 1:
                result = 0
                break
    for a in range(0,9,3):
        for b in range(0,9,3):
            x = [0] * 10
            for c in range(3):
                for d in range(3):
                    x[S[a+c][b+d]] += 1

            for e in range(1,9):
                if x[e] !=1:
                    result = 0
                    break

    print(f"#{test_case} {result}")

