class Solution:
    # @param A : list of integers
    # @return a list of integers
    def QuickSort(self,A,l,r):

        if l >= r:
            return

        ele = A[l]
        i = l + 1
        j = r

        while i<=j:
            if A[i]<=ele:
                i += 1
            elif A[j]>ele:
                j -= 1
            else:
                A[i],A[j] = A[j],A[i]
                i += 1
                j -= 1

        A[l],A[i-1] = A[i-1],A[l]
        self.QuickSort(A,l,i-2)           
        self.QuickSort(A,i,r)           


    def solve(self, A):
        self.QuickSort(A,0,len(A)-1)
        return A

s = Solution()
s.solve([5,4,7,8,4,1,3])
