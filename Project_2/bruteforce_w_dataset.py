'''inversion count in n time: input dataset file path before running'''
#Diana Cervantes
import time

file_path = "D:\CodingProjects\school\AnalysisOfAlgorithms\Project_2\dataset.txt"
file =  open(file_path, "r")

dataset = file.readlines()

def inversion_check(arr, n):
    '''Checking the amount of Inversions'''
    inversions = 0
    for i in range(n):
        for j in range(i +1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions


start = time.time()
print(f'Array length: {len(dataset)}')
#Taking the file/dataset and running the inversion check.
print(f'Number of inversions: {inversion_check(dataset, len(dataset))}')
end = time.time()
print(f'Runtime: {end-start} seconds')

## TEST CASE:
#54044 14108 79294 29649 25260 60660 2995 53777 49689 9083

## DATASET RESULTS:
#Array length: 100000
#Number of inversions:
#Runtime:
