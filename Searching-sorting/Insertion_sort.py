def insertion_sort(array):
    length = len(array)

    for i in range(1, length):

        current_element = array[i]
        position = i

        while position > 0 and array[position-1] > current_element:

            array[position] = array[position - 1]
            position = position - 1

        array[position] = current_element

    return array

arr = [10,9,8,7,6,5,4,3,2,1]
print(insertion_sort(arr))
