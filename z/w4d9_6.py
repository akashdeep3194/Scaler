class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        arr = A
        m = len(arr)
        for r in range(m):
            for c in range(m):
                if r==c:
                    if arr[r][c] == 1:
                        continue
                    else:
                        return 0
                elif arr[r][c] != 0:
                    return 0
        return 1

# s = Solution()
# a =  [[1, 0, 0],[0, 1, 0],[0, 1, 2]]
# print(s.solve(a))
