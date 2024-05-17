T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    speed = 0
    move = 0
    for i in range(N):
        a = list(map(int,input().split()))
        if a[0] == 1:
            speed += a[1]
        elif a[0] == 2:
            if a[1] > speed:
                speed = 0
            else:
                speed -= a[1]
        move += speed
    print(f"#{test_case} {move}")