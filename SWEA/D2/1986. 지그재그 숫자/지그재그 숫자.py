T = int(input())
for i in range(1,T+1):
    N = int(input())
    answer = 0
    for j in range(1,N+1):
        if j%2 == 0:
            answer -= j
        else:
            answer += j
    print(f"#{i} {answer}")