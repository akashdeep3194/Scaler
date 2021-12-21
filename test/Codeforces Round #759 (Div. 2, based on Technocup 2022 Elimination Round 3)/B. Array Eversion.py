import sys

def solve(arr):
    mx = max(arr)
    ans = 1
    i = 0
    last = arr[-1]
    if arr[-1] == mx:
        return 0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == mx:
            return ans
    
        if arr[i]>last:
            ans += 1
            last = arr[i]
    return ans

t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = list(map(int,sys.stdin.readline().strip().split()))
    print(solve(arr))
