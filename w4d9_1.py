class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        a=A
        m = len(a)
        n = len(a[0])

        for r in range(m):
            for c in range(r+1,n):
                if a[r][c] == 0:
                    continue
                else:
                    return 0
        return 1

# s = Solution()
# arr = [[0, 2],
#       [0, 0]]
# print(arr)
# print(s.solve(arr))
