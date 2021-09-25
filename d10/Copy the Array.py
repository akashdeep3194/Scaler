class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        arr = []
        for ele in A:
            arr.append(ele+B)
        return arr