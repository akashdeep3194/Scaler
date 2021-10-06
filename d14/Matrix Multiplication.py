class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        ans = [[0 for ele in range(len(B[0]))] for _ in range(len(A))]
        s = 0

        for i in range(len(A)):
            for k in range(len(B[0])):
                for j in range(len(A[0])):
                    s += A[i][j]*B[j][k]
                ans[i][k] = s
                s = 0
        return ans

# s = Solution()

# A = [[1, 2],[3, 4]]

# B = [[5, 6],[7, 8]]            

# print(s.solve(A,B))
