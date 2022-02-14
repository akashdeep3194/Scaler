# arr = [1, 7, 0, 0, 8, 0, 10, 12, 4, 5, 0]

# ans = [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]


def move_zeroes(arr):
    ans = []
    ctr = 0

    for ele in arr:
        if ele == 0:
            ctr += 1
        else:
            ans.append(ele)
    while ctr > 0:
        ans.append(0)
        ctr -= 1
    return ans


def swap_till_zero(arr, i, n):
    i += 1
    while i < n:
        if arr[i] != 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        i += 1
    return


def move_zeros_better_sc(arr):
    n = len(arr)
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            swap_till_zero(arr, i, n)
    return arr

arr = [1, 7, 0, 0, 8, 0, 10, 12, 4,0, 5]
print(move_zeros_better_sc(arr))
