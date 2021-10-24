class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A,reverse=True)
        ans = 0
        for i,ele in enumerate(A):
            ans += ele*(i+1)
        return ans
