T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    sl = []
    for i in range(N):
        S, num = input().split()
        for j in range(int(num)):
            sl.append(S)
    print(f"#{test_case}",end="")
    for j in range(len(sl)):
        if j % 10 == 0:
            print()
        print(sl[j],end="")
    print()

