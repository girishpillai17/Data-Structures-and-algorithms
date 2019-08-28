def bubble_sort(array):
    n = len(array)

    for i in range(n-1,0,-1):

        for j in range(i):

            if array[j] > array[j+1]:

                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            
            else:
                break

    return array

arr = [10,9,8,7,6,5,4,3,2,1]
print(bubble_sort(arr))
