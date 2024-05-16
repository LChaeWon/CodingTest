C = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
T = int(input())
for test_case in range(1,T+1):
    day = 0
    cm, cd, fm, fd = map(int,input().split())
    if cm == fm:
        day = fd - cd + 1
    else:
        for i in range(cm+1, fm):
            day += C[i]
        day = day + (C[cm] - cd + 1) + fd

    print(f"#{test_case} {day}")