class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B, si=0, s=0):

        if s > 1000:
            return 0
        if B == 0:
            if s <= 1000:
                return 1
            else:
                return 0
        if len(A) <= si:
            return 0
        x = self.solve(A, B-1, si+1, s+A[si])
        y = self.solve(A, B, si+1, s)

        return x+y


if __name__ == '__main__':
    s = Solution()
    print(s.solve([1, 2, 8], 2))
