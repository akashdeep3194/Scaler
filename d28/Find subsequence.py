class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        j = i = 0
        while i<len(A) and j<len(B):
            if A[i] == B[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i == len(A):
            return "YES"
        else:
            return "NO"
