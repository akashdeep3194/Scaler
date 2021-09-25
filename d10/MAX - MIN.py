class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        a = sorted(A)
        b = B
        n = len(a)
        ans = a[n-b] - a[b-1]
        return ans