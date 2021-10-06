def thirdMax(A):
    fmax = 0
    smax = 0
    tmax = 0
    for i in range(len(A)):
        if A[i]>=fmax:
            tmax = smax
            smax = fmax
            fmax = A[i]
        elif smax<=A[i]<=fmax:
            tmax = smax
            smax = A[i]
        elif tmax<=A[i]:
            tmax = A[i]
    return tmax
        

