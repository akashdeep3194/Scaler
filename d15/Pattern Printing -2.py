class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):

        ans = [[0 for _ in range(A)]for _ in range(A)]

        for i in range(A):
            for j in range(A):
                if j+i>=A-1:
                    ans[i][j] = A-j
        return ans

# s = Solution()
# print(s.solve(4))
