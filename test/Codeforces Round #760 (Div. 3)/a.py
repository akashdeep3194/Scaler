import sys

def solve(arr):

    ans = []
    c = arr[-1] - arr[0] - arr[1]
    ans.extend([arr[0],arr[1],c])    
    return ans

t = int(input())

while t>0:
    t -= 1
    arr = list(map(int,sys.stdin.readline().strip().split()))
    ans = solve(arr)
    print(ans[0],ans[1],ans[2])
