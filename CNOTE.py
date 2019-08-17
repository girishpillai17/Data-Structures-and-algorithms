T = int(input())
for i in range(T):
    x, y, k, n = map(int, input().split())
    for i in range(n):
        Pi, Ci = map(int, input().split())
        if Pi >= (x-y) and Ci <= k:
            print("Luckychef")
            break
    else:
        print("Unluckychef")