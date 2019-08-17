def cyclic_rotate(arr, n):
    x = arr[n-1]

    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = x

arr = list(range(6))
print("The input array is", arr)
n = len(arr)

cyclic_rotate(arr, n)
print("The output array is", arr)
