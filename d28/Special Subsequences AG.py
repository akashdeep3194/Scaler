class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        cg = 0
        c = 10**9+7
        ans = 0
        for i in range(len(A)-1,-1,-1):
            if A[i] == 'G':
                cg += 1
            elif A[i] == 'A':
                ans += cg
            if ans>c:
                ans = ans%c
        return ans%c
