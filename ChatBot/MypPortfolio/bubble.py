def count_swaps(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return swaps

def min_swaps_to_beautiful_array(n, arr):
    ascending_swaps = count_swaps(arr.copy())
    descending_swaps = count_swaps(arr[::-1])

    return min(ascending_swaps, descending_swaps)

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
result = min_swaps_to_beautiful_array(n, arr)
print(result)
