for test_case in range(10):
    N = int(input())
    H = list(map(int,input().split()))
    for i in range(N):
        a = H.index(max(H))
        b = H.index(min(H))
        H[a] -= 1
        H[b] += 1
    print(f"#{test_case+1} {max(H)-min(H)}")




