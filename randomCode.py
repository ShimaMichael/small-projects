from collections import defaultdict


nums = [1, 2, 3, 4]
n = len(nums)
for i in range(n-1, -1, -1):
    i+=1
    #print(nums[i])

directions = (4,5,5,3)
d = 0
for i in range(16):
    #print(d)
    d = (d + 1) % 4
    
print(1 | 1)
print(1 ^ 1)
print((1 & 1) << 1)

word = "haystack"
n = 2
for i in range(len(word)-n+1):
    print(i)
    print(word[i:i+n])
sample = ["gg", "hell"]
string = "hello"
wordTuple = tuple(sorted(string))
sample.sort()
print(wordTuple)
print(sorted(string))
print(sample)
print(tuple([1]*26))

NA = [1,2,3,4]
nested = [[] for i in range(len(NA)+1)]
print(nested)


print(ord('H') - ord('A'))

print(string[0:3])


"""
#include <stdio.h>

// Function to swap two elements
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Partition function
int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // Choosing the last element as the pivot
    int i = low - 1;        // Index for the smaller element

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {  // If the current element is smaller than or equal to the pivot
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

// QuickSort function
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);  // Partition index
        quickSort(arr, low, pi - 1);         // Sort the elements before the partition
        quickSort(arr, pi + 1, high);        // Sort the elements after the partition
    }
}

// Utility function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Main function
int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    printArray(arr, n);

    quickSort(arr, 0, n - 1);

    printf("Sorted array: ");
    printArray(arr, n);

    return 0;
}


#include <stdio.h>

// Function to merge two subarrays
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    // Create temporary arrays
    int L[n1], R[n2];

    // Copy data to temporary arrays
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Merge the temporary arrays back into arr[l..r]
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Merge Sort function
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);       // Sort the first half
        mergeSort(arr, m + 1, r);  // Sort the second half
        merge(arr, l, m, r);       // Merge the sorted halves
    }
}

// Utility function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Main function
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    printArray(arr, n);

    mergeSort(arr, 0, n - 1);

    printf("Sorted array: ");
    printArray(arr, n);

    return 0;
}
"""
