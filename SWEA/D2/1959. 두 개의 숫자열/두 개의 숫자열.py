T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if len(A) > len(B):
        Max = A
        Min = B
    else:
        Max = B
        Min = A
    k = []
    for i in range(len(Max)-len(Min)+1):
        answer = []
        for j in range(len(Min)):
            answer.append(Min[j]*Max[i+j])
        k.append(sum(answer))
    print(f"#{test_case} {max(k)}")