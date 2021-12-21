import sys

def solve(arr):

    ans = 1
    
    for i,ele in enumerate(arr):

        if i>=1:

            if arr[i-1]>0 and arr[i]>0:
                ans += 5
            elif arr[i-1] == 0 and arr[i] == 0:
                ans = -1
                break
            elif arr[i] == 1:
                ans += 1

        elif arr[i] == 1:
            ans += 1

    return ans

t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = list(map(int,sys.stdin.readline().strip().split()))
    print(solve(arr))

