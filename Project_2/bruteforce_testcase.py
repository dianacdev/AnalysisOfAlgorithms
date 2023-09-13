'''inversion count in n time: input smaller test case arrays'''
#Diana Cervantes
import time

def inversion_check(arr, n):
    '''Checking the amount of Inversions'''
    inversions = 0
    for i in range(n):
        for j in range(i +1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

array = []
array = [int(item) for item in input("Enter an list of values: ").split()]
length = len(array)
print(f'Array: {array}')

start = time.time()

print(f'Number of inversions: {inversion_check(array, length)}')
end = time.time()
print(f'Runtime: {end-start}')

## TEST CASE:
#54044 14108 79294 29649 25260 60660 2995 53777 49689 9083
