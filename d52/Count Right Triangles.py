class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        z = 10**9+7
        ctr = 0
        dcx = dict()
        dcy = dict()
        for i in range(len(A)):
            dcx[A[i]] = dcx.get(A[i], 0) + 1
            dcy[B[i]] = dcy.get(B[i], 0) + 1
        for i in range(len(A)):
            l = dcx[A[i]]-1
            r = dcy[B[i]]-1
            ctr = (ctr + (l*r) % z) % z
        return ctr


if __name__ == "__main__":
    s = Solution()
    A = [1, 1, 2, 3, 3]
    B = [1, 2, 1, 2, 1]
    print(s.solve(A, B))
