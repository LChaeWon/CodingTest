T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    A = [list(map(int,input())) for _ in range(N)]
    answer = 0
    b = N // 2
    k = b-1
    for i in range(N):
        if i <= b:
            for j in range(b-i,b+i+1):
                answer += A[i][j]
        else:
            for q in range(b-k,b+k+1):
                answer += A[i][q]
            k -= 1
    print(f"#{test_case} {answer}")
