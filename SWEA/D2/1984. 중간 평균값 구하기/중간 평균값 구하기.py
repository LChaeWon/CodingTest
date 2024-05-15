T = int(input())
for test_case in range(1,T+1):
    N = list(map(int,input().split()))
    N.remove(min(N))
    N.remove(max(N))
    a = 0
    for i in N:
        a += i
    print(f"#{test_case} {round(a/len(N))}")