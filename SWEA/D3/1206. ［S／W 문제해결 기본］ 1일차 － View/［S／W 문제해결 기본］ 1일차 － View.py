for n in range(10):
    N = int(input())
    H = list(map(int,input().split()))
    num = 0
    answer = 0
    for i in range(2,N-2):
        if H[i-2] > H[i] or H[i-1] > H[i] or H[i+1] > H[i] or H[i+2] > H[i]:
            continue
        a = H[i]-H[i-2]
        b = H[i]-H[i-1]
        c = H[i]-H[i+1]
        d = H[i]-H[i+2]
        num = min(a,b,c,d)
        answer += num
    print(f"#{n+1} {answer}")