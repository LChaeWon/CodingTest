M = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}
T =int(input())
for i in range(1, T+1):
    A = int(input())
    for j in M.keys():
        M[j] = A//j
        A = A%j

    print(f"#{i}")
    for k in M.values():
        print(k,end=" ")
    print()
    M = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}