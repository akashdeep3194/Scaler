class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mx = mn = A[0]

        for ele in A:
            if ele>mx:
                mx = ele
            if ele<mn:
                mn = ele
        return mx + mn