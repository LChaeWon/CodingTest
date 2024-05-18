T = int(input())
for test_case in range(T):
    N = int(input())
    score = list(map(int,input().split()))

    M = [0]*101
    max = 0
    s = 0
    for i in range(1000):
        M[score[i]] += 1
    for k in range(len(M)):
        if max <= M[k]:
            max = M[k]
            s = k

    print(f"#{N} {s}")