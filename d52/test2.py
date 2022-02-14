arr = [1, None, 2, 3, None, None, 5, None]
ans = [1, 1, 2, 3, 3, 5, 5]


def fill_None(arr):
    for i, ele in enumerate(arr):
        l, ele_l = checkleftnearest(arr, i)
        r, ele_r = checkrightnearest(arr, i)
        if r < l:
            arr[i] = ele_r
        else:
            arr[i] = ele_l
