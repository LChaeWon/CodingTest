T = int(input())
for i in range(1, T+1):
    a = input()
    p = ""
    for j in range(len(a)):
        p += a[j]
        if p == a[j+1:j+1+len(p)]:
            print(f"#{i} {len(p)}")
            break



