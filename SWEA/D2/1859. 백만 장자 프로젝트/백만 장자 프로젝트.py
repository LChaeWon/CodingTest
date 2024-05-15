T = int(input())
for i in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    price = 0
    answer = 0
    for j in A[::-1]:
        if j >= price:
            price = j
        else:
            answer = answer+ price - j
    print(f"#{i} {answer}")


