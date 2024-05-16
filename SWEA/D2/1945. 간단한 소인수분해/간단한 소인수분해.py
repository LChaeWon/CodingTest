T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    K = [2, 3, 5, 7, 11]
    A = [0, 0, 0, 0, 0]
    i = 0
    while(N!=0):
        if i == 5:
            break
        if N % K[i] == 0:
            A[i] += 1
            N = N//K[i]
        else:
            i += 1
    print(f"#{test_case}",end=" ")
    for k in range(5):
        print(A[k],end=" ")
    print()