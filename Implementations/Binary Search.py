def binarySearch(a: list, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

a = [1, 3, 5, 6, 9, 10, 11]

if __name__ == "__main__":
    print(binarySearch(a, 7))
    print(binarySearch(a, 3))
    print(binarySearch(a, 9))
    assert binarySearch(a, 9) == 4
    assert binarySearch(a, 3) == 1
    assert binarySearch(a, 7) == -1
