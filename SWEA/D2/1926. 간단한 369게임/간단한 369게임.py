N = int(input())
for i in range(1,N+1):
    a = str(i)
    n = a.count("3") + a.count("6") + a.count("9")
    if n == 0:
        print(i,end=" ")
    else:
        print("-"*n , end=" ")