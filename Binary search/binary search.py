arr = [3,5, 15, 30,67,553]

def binarySearch(arr: list[int], target:int) -> int:
    right = len(arr) - 1
    left  = 0
    while left <= right:
        middle = int(left + (right - left) / 2)
        print(middle)
        if arr[middle] == target:
            return middle
        if arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(binarySearch(arr, 553))
print(5/2)
print(5//2)


#int *arr = (int*)malloc(size * sizeof(int))