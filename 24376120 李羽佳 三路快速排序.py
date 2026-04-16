def quick_sort_3_ways(arr, low, high):
    if low >= high:
        return
    pivot = arr[low]
    lt = low
    gt = high
    i = low + 1
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    quick_sort_3_ways(arr, low, lt - 1)
    quick_sort_3_ways(arr, gt + 1, high)
test_arr = [2, 0, 2, 1, 1, 0]
quick_sort_3_ways(test_arr, 0, len(test_arr) - 1)
print("三路排序结果:", test_arr)