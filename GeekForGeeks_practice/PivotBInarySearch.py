#program to find the pivot number
def find_pivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high)/2)                           # arr = [3,4,5,6,1,2], mid = 3(6), low=0, high=5

    if mid < high and arr[mid] > arr[mid+1]:            #if 3 < 5 && 6>1   
        return mid
    
    if mid > low and arr[mid] < arr[mid-1]:             #if 3 > 0 && 6 < 5
        return (mid-1)

    if arr[low] >= arr[mid]:                            #if 3 >= 6
        return find_pivot(arr, low, mid-1)
    else:
        return find_pivot(arr, mid+1, high)             #if 3 <= 6


#binary search
def binarysearch(arr,low,high,key):
    if high < low:
        return -1

    mid = int((low + high)/2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarysearch(arr, (mid+1), high, key)
    else:
        return binarysearch(arr, low, (mid-1), key)
        
#pivotbinarysearch
def pivotedBinarySearch(arr, n, key):
    
    pivot = find_pivot(arr, 0, n-1)

    if pivot == -1:
        return binarysearch(arr, 0, n-1, key)

    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarysearch(arr, 0, pivot-1, key)
    else:
        return binarysearch(arr, pivot+1, n-1, key)


arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3] 
n = len(arr1) 
key = 10
print("Index of the element is : ",  
      pivotedBinarySearch(arr1, n, key))

