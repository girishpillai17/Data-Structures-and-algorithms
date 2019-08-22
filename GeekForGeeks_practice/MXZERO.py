T = int(input())
for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    C1 = []
    C0 = []
    for j in lst:
        if j == 1:
            C1.append(j)
        else:
            C0.append(j)
    if (len(C1)) % 2 != 0:
        print(len(C1))
    else:
        print(N - len(C1))

    #(C1)
    #print(C0)
    #print(len(C1))
    #print(N - len(C1))



