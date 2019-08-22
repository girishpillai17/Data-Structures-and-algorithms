n = int(input('no of elements: '))
arr = list(range(n))
print(arr)
for i in range(n//2 - 1):
    temp = arr[0:2]
    print(temp)
    arr = arr[2:n + 1]
    print(arr)
    for i in temp:
        arr.append(i)
    print(arr)
