'''inversion count input'''
#Diana Cervantes
import time

#providing the file path, where the dataset text is located.
file_path = "D:\CodingProjects\school\AnalysisOfAlgorithms\Project_2\dataset.txt"
file =  open(file_path, "r")

dataset = file.readlines()

def merge_sort(arr, n):
    '''Creates a temp array used in the merge function, and calls inversion_merge_sort'''
    temp_arr = [0]*n
    return inversion_merge_sort(arr, temp_arr,0, n - 1)

def inversion_merge_sort(arr, temp_arr, left, right):
    """Counts the inversions using merge sort, returns the inversion count."""
    inv_count = 0

    if left < right:
        mid = (left + right)//2
        #Calculating Inversions in left subarray
        inv_count += inversion_merge_sort(arr, temp_arr,left, mid)

        #Calculating Inversions in right subarray
        inv_count += inversion_merge_sort(arr, temp_arr,mid + 1, right)

        #Merging two subarrays into a single sorted array.
        inv_count += merge(arr, temp_arr,left, mid, right)

    return inv_count

def merge(arr, temp_arr, left, mid, right):
    '''Function merges two subarrays into a single array that is sorted'''
    #Creating left subarray
    i = left

    #Creating left subarray
    j = mid + 1

    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
    return inv_count

start = time.time()
print(f'Array length: {len(dataset)}')
#Taking the file/dataset and running the inversion check.
print(f'Number of inversions: {merge_sort(dataset, len(dataset))}')
end = time.time()
print(f'Runtime: {end-start} seconds')

## TEST CASE:
#54044 14108 79294 29649 25260 60660 2995 53777 49689 9083

## DATASET RESULTS:
#Array length: 100000
#Number of inversions:
#Runtime:
