class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        ans = [ele[:] for ele in (A)]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    for k in range(len(A[0])):
                        ans[i][k] = 0
                    for k in range(len(A)):
                        ans[k][j] = 0
        return ans
