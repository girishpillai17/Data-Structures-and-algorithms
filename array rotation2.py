n = int(input('no of elements: '))
temp = arr[0]
for i in range(n-2):
    arr[i] = arr[i+1]
arr.append(temp)
print(arr)