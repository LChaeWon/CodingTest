T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    P = [list(map(int,input().split())) for i in range(N)]
    result = 0

    for i in range(N):
        sum = 0

        for j in range(N):
            if P[i][j] == 1:
                sum += 1
            if P[i][j] == 0 or j == N-1:
                if sum == K:
                    result += 1
                sum = 0
        for k in range(N):
            if P[k][i] == 1:
                sum += 1
            if P[k][i] ==0 or k == N-1:
                if sum == K:
                    result += 1
                sum = 0
    print(f"#{test_case} {result}")