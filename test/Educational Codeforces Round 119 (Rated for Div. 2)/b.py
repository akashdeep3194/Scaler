import sys

def solve(arr,n):

    oc = tc = thc = 0

    for ele in arr:
        thc = max(thc,ele//3)
        if ele%3 == 1:
            oc = 1
        elif ele%3 == 2:
            tc = 2
            oc = 0
    
    if oc == 1 and tc == 1 and thc == ele/3:
        thc = max(0,thc-1)

    return oc+tc+thc


t = int(input())
while t>0:
    n = int(input())
    t -= 1
    arr = list(map(int,(sys.stdin.readline().strip().split())))
    ans = solve(arr,n)
    print(ans)
