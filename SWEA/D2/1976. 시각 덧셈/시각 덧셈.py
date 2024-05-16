T = int(input())
for i in range(1,T+1):
    a, b, c, d = map(int,input().split())
    H = a + c
    M = b + d
    if M >= 60:
        M -= 60
        H += 1
    if H > 12:
        H  -= 12
    print(f"#{i} {H} {M}")