class Solution:
    # @param A : list of list of integers

    def solve(self, A):
        n = len(A)
        m = len(A[0])

        # Clock wise

        for i in range(n):
            for j in range(i+1,m):
                A[i][j],A[j][i] = A[j][i],A[i][j]

        for ele in A:
            for i in range(m//2):
                ele[i],ele[m-1-i] = ele[m-1-i],ele[i]

        # Anti Clockwise
        # for i in range(n):
        #     for j in range(i+1,m):
        #         A[i][j],A[j][i] = A[j][i],A[i][j]

        # for i in range(n//2):
        #     A[i],A[n-1-i] = A[m-1-i],A[i]
        return A

s = Solution()
A = [[1, 2],[3, 4]]
print(s.solve(A))
