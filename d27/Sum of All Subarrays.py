class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        n = len(A)
        s = 0
        for i,ele in enumerate(A):
            s += (i+1)*(n-i)*A[i]
        return s
