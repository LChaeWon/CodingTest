T = int(input())
for i in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())
    A, B = 0, 0
    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + (W-R) * S

    print(f"#{i} {min(A,B)}")