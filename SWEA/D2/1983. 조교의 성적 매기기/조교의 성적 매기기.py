T = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for test_case in range(1,T+1):
    N, K = map(int, input().split())
    b = []
    for _ in range(N):
        a = list(map(int,input().split()))
        ave = a[0]*0.35 + a[1]*0.45 + a[2]*0.2
        b.append(ave)
    score = b[K-1]
    b.sort(reverse=True)
    div = N//10
    final = b.index(score)//div
    print(f'#{test_case} {grade[final]}')