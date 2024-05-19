for test_case in range(1,11):
    N = int(input())
    A = list(map(int,input().split()))

    while 1:
        if A[len(A)-1] == 0:
            break
        else:
            j = 1
        while j < 6:
            if A[0] - j <= 0:
                A.append(0)
                del A[0]
                break
            else:
                A.append(A[0] - j)
                del A[0]
                j += 1
    print(f"#{test_case}",end=" ")
    for i in A:
        print(f"{i}", end=" ")
    print()
