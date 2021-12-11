class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        sm = 0
        for ele in A:
            sm += ele
        if sm&1 == 0:
            return "Yes"
        else:
            return "No"
