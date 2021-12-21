import sys

def solve(arr):
    cn = 0
    for ele in arr:
        if ele == 'N':
            cn += 1
    if cn == 1:
        ans = "NO"
    else:
        ans = "YES"
    return ans
    
t = int(input())

while t>0:
    t -= 1
    arr = input()
    ans = solve(arr)
    print(ans)
