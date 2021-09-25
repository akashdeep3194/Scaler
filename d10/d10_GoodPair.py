class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        a=A
        b=B
        n = len(a)
        for i in range(n):
            for j in range(i+1,n):
                if a[i]+a[j] == b:
                    return 1
        return 0

    def solve_sorted(self, A, B):
        a=sorted(A)
        b=B
        n = len(a)
        i=0
        j=n-1
        while i<j:
            if a[i]+a[j] == b:
                return 1
            elif a[i]+a[j]>b:
                j-=1
            else:
                i+=1            
        return 0
