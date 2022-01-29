import sys
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        mn = sys.maxsize
        ind = 0
        for i in range(len(A)):
            mn = A[i]
            ind = i
            for j in range(i,len(A)):
                if A[j]<mn:
                    mn = A[j]
                    ind = j
            A[i],A[ind] = A[ind],A[i]

            if i == B-1:
                return A[i]
        return
if __name__ == '__main__':
    s = Solution()
    A = [ 94, 87, 100, 11, 23, 98, 17, 35, 43, 66, 34, 53, 72, 80, 5, 34, 64, 71, 9, 16, 41, 66, 96 ]
    B = 19
    print(s.kthsmallest(A,B))
