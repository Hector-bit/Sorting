# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if(arr[j] < arr[smallest_index]):
                smallest_index = j
        temp_arr = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp_arr
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # set the outer loop, size of where numbers get bubbled
    for i in range(len(arr)-1, 0, -1):
        for x in range(0, i):
            # check if the left is bigger than the right
            if arr[x] > arr[x+1]:
                # if yes, move it to the right
                temp = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr