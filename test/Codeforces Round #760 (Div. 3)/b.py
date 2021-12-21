import sys
from typing import List

def solve(arr:List,n):

    ans = ''
    ans = arr[0][0]+ arr[0][1]
    k = len(arr)
    i = 1
    while i<k:
        ele = arr[i]

        if ele[0] != arr[i-1][1]:
            ele = arr[i-1][1]+ele[0]
            arr.insert(i,ele)

        ans += ele[1]
        
        k = len(arr)
        i += 1
            
    if len(ans) == n:
        return ans
    else:
        return ans+'a'

t = int(input())


while t>0:

    t -= 1
    n  = int(input())
    arr = list(sys.stdin.readline().strip().split())
    # arr = ['ab','bb','ba','aa','ab']
    ans = solve(arr,n)
    print(ans)
