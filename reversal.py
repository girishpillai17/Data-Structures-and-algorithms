def reversearray(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]       
        arr[end] = temp
        start += 1                  #Increase towards right
        end -= 1                    #Decrease towards left

def rotate(arr, d):
    n = len(arr)
    A = reversearray(arr, 0, d-1)
    print(arr)
    B = reversearray(arr, d, n-1)
    print(arr)
    C = reversearray(arr, 0, n-1)

arr = [1,2,3,4,5,6,7]
rotate(arr, 2)
print(arr)