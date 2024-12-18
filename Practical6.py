#Sort the array using Radix Sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array that will hold the sorted numbers
    count = [0] * 10  # Count array for digits (0 to 9)

    # Count occurrences of each digit in the specified place (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Apply counting sort to sort elements based on each digit
    exp = 1  # Exponent representing the current digit place (1, 10, 100, ...)
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to the next digit place

# Example usage
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", arr)
    radix_sort(arr)
    print("Sorted array:", arr)