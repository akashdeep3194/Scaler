class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        mx = max(A)
        spf = [2 for i in range(mx+1)]
        spf[1] = 1
        i = 2

        while i<=mx:
            j = i*2
            while j<=mx:
                spf[j] += 1
                j += i
            i += 1

        res = []
        for ele in A:
            res.append(spf[ele])
        return res
