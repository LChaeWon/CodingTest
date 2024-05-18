T = int(input())
for test in range(1,T+1):
    print(f"#{test}",end=" ")
    N, M = map(int,input().split())
    A = [input() for _ in range(N)]
    d = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
         '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
    i = 0
    q = 0
    while 1:
        if '1' in A[i]:
            c = A[i]
            break
        i += 1
    for j in range(len(c)-1,-1,-1):
        if c[j] == '1':
            q = j
            break

    z =[]
    p = []
    for k in range(q,-1,-7):
        z.append(c[k-6:k+1])
    for g in range(len(z)):
        if z[g] in d:
            p.append(d[z[g]])
    a = ((p[7] + p[5] + p[3] + p[1])*3) + p[0]+p[2]+p[4]+p[6]
    if a % 10 == 0:
        print(sum(p))
    else:
        print(0)