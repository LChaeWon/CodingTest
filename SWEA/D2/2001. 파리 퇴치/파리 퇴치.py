T = int(input())
for s in range(1,T+1):
    N, M = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(N)]

    kills = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for k in range(M):
                for l in range(M):
                    fly += a[i+k][j+l]
            kills.append(fly)
    print(f"#{s} {max(kills)}")