class Solution:
    # @param A : list of integers
    # @return an integer

    def solveH(self, A, l, r):
        m = l + (r-l+1)//2        
        x = self.solveH(A,l,m-1)
        y = self.solveH(A,m,r)
        
        temp = [0]*(r-l+1)
        i = l
        j = m
        k = 0
        
        while i<m and j<=r:
            if A[i]<=A[j]:
                i += 1
                
        
        
    def solve(self, A):
        self.solveH(A,0,len(A)-1)