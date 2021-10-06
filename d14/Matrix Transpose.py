class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        ans = [[0 for ele in range(len(A))] for ele in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans[j][i] = A[i][j]
        return ans

# s = Solution()
# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# print(s.solve(A))
