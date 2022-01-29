class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        arr = [[0 for _ in range(A)] for _ in range(A)]
        for i in range(1, A + 1):
            for j in range(1, A + 1):
                if i >= j:
                    arr[i-1][j-1] = j
        return arr


s = Solution()
print(s.solve(3))
