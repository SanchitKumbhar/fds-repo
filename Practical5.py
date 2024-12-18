arr = [90, 80, 70, 60, 50, 40, 30, 20, 10]

#Using Selection Sort
def selection_sort(arr):
    for i in range (len(arr)-1):
        min_index = i

        for j in range (i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

print("Unsorted array1 = ", arr)
selection_sort(arr)
print("Sorted array using selection sort = ", arr)

#Using Bubble sort

arr1 = [99, 88, 77, 66, 55, 44, 33, 22, 11]
def bubble_sort(arr1): 
    for i in range (len(arr1)):
        for j in range (0, len(arr1)-i-1):
            if arr1[j] > arr1[j+1]:
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]

print("Unsorted array2 = ", arr1)
bubble_sort(arr1)
print("Sorted array using bubble sort = ", arr1)

top_5_scores = arr1[-5:]
print("The top 5 scores are = ", top_5_scores)