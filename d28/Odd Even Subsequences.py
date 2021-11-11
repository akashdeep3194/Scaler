class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        olen = elen = 0
        prevo = 0
        preve = 0

        for i in range(len(A)):
            if prevo == 0 and A[i]&1 == 1:
                olen += 1
                prevo = 1
            if prevo == 1 and A[i]&1 == 0:
                olen += 1
                prevo = 0

        for i in range(len(A)):
            if preve == 0 and A[i]&1 == 0:
                elen += 1
                preve = 1
            if preve == 1 and A[i]&1 == 1:
                elen += 1
                preve = 0

        return max(olen, elen)
